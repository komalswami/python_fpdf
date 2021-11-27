#pip install fpdf
from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from fpdf import FPDF
#from create_table_fpdf import PDF

data = [['First name', 'Last name', 'Age', 'City'],
        ['Jules', 'Smith', 34, 'San Juan'],
        ['Mary', 'Ramos', 45, 'Orlando'], [
            'Carlson', 'Banks', 19, 'Los Angeles']
        ]

data_as_dict = {"First name": ["Jules","Mary","Carlson","Lucas"],
                "Last name": ["Smith","Ramos","Banks","Cimon"],
                "Age": [34,'45','19','31']
            }



class PDF(FPDF):
    def header(self):
        self.image('logosmall.png',10,8,33)
        self.set_font('Arial','B',15)
        self.cell(80)
        #self.cell(30,10,'Service Book Manager',1,0,'C')
        self.cell(30,10,'Service Book Manager')
        self.ln(20)
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        self.cell(0,10,f'page{self.page_no()}',align='C')

#def export():
 #   pdf = FPDF()
  #  pdf.add_page()
   # pdf.set_font("Arial", "", 16)
   # pdf.cell(40, 10, textbox.get("1.0", END).strip())
   # pdf.output(asksaveasfilename(filetypes=[("PDF file", "*.pdf")]), "F")


#root = Tk()
#root.title("Text2PDF")
#textbox = ScrolledText(root)
#textbox.pack(fill=BOTH, expand=YES)
#Button(root, text="Export to PDF", command=export).pack(fill=X)
pdf = PDF()

pdf.add_page()
pdf.set_font("Arial", "", 16)

# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw / 4

th = pdf.font_size

pdf.ln(4 * th)

#pdf.cell(40, 10, textbox.get("1.0", END).strip())
pdf.cell(0,10,'name of the staff',ln=True)
pdf.cell(0,10,'address',ln=True)
pdf.cell(0,10,'position',ln=True)
pdf.cell(0,10,'joined from',ln=True)
pdf.cell(0,10,'joined to',ln=True)


pdf.add_page()
pdf.ln(4 * th)
pdf.ln()
for row in data:
    for datum in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(col_width, th, str(datum), border=1)

    pdf.ln(th)

pdf.add_page()
pdf.ln(4 * th)
pdf.set_font('Times', 'B', 14.0)
pdf.cell(epw, 0.0, 'With more padding', align='C')
pdf.set_font('Times', '', 10.0)
pdf.ln(2*th)

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2 * th, str(datum), border=1)

    pdf.ln(2 * th)

#pdf.output(asksaveasfilename(filetypes=[("PDF file", "*.pdf")]), "F")
pdf.output('pdf2.pdf')
#pdf.add_page()
#root.mainloop()





