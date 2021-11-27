#Getting started

```
pip install fpdf
pip install fpdf2
```

### import 


### create fpdf object

1. Layout :('P','L')
2. Unit :('mm','cm','in')
3. Format :('A3','A4(default)','A5','Letter','Legal',(w,h) eg (100,150))

pdf=FPDF('P','mm','Letter') 

deault one
pdf=FPDF()

add a page
pdf.add_page()

### specify font
### fonts :('times','courier','helvetica','Symbol','Zpfdingbats')
### 'B'(bold),'U'(underline),'I'(italics),''regular,combination i.e ('IB')
### size of font

pdf.set_font('helvetica','',16)

### add text
### w= width 1st argument
### h=height 2nd argument
pdf.cell(40,10,'Hello world!')

### line break ln=true and false for next line
### align for alignment
### border (0 false;1 true -add border around cell)
pdf.cell(0,10,'hello world',align='C',ln=True)

### pdf export 
pdf.output('name of pdf.pdf')


### adding header and footer

### we have to extend exsiting FPDF class and edit header and footer content
class PDF(FPDF):
    def header(self):
        self.image('logosmall.png',10,8,33)
        self.set_font('Arial','B',15)
        self.cell(80)
        #self.cell(30,10,'Service Book Manager',1,0,'C')
        self.cell(30,10,'Service Book Manager')
        self.ln(20)
    def footer(self):
        ### adding page no 
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        self.cell(0,10,f'page{self.page_no()}',align='C')



### custum name ask at the time of saving the pdf file
pdf.output(asksaveasfilename(filetypes=[("PDF file", "*.pdf")]), "F")
