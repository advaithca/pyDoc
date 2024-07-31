from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

class PDFCreator:
    def __init__(self, filename, font_size=11):
        self.filename = filename
        self.font_size = font_size
        self.styles = self.get_styles()
        self.story = []

    def get_styles(self):
        styles = getSampleStyleSheet()
        
        # Modify existing styles to use Times New Roman
        styles['Title'].fontName = 'Times-Roman'
        styles['Title'].fontSize = 24
        styles['Title'].leading = 28
        styles['Title'].alignment = TA_CENTER
        
        styles['Heading1'].fontName = 'Times-Roman'
        styles['Heading1'].fontSize = 18
        styles['Heading1'].leading = 22
        styles['Heading1'].spaceAfter = 10
        
        styles['Heading2'].fontName = 'Times-Roman'
        styles['Heading2'].fontSize = 14
        styles['Heading2'].leading = 18
        styles['Heading2'].spaceAfter = 10
        
        styles['BodyText'].fontName = 'Times-Roman'
        styles['BodyText'].fontSize = self.font_size
        styles['BodyText'].leading = self.font_size + 4
        styles['BodyText'].spaceAfter = 10
        styles['BodyText'].alignment = TA_JUSTIFY
        
        return styles

    def add_title(self, title):
        self.story.append(Paragraph(title, self.styles['Title']))
        self.story.append(Spacer(1, 12))

    def add_heading1(self, heading):
        self.story.append(Paragraph(heading, self.styles['Heading1']))
        self.story.append(Spacer(1, 12))

    def add_heading2(self, heading):
        self.story.append(Paragraph(heading, self.styles['Heading2']))
        self.story.append(Spacer(1, 12))

    def add_paragraph(self, text):
        self.story.append(Paragraph(text, self.styles['BodyText']))
        self.story.append(Spacer(1, 12))

    def save(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
        doc.build(self.story)

# Usage example:
if __name__ == "__main__":
    pdf = PDFCreator("example.pdf", font_size=12)
    pdf.add_title("Sample Document")
    pdf.add_heading1("Introduction")
    pdf.add_paragraph("This is a sample paragraph in the introduction section. This text is styled similarly to LaTeX's article class with Times New Roman font.")
    pdf.add_heading2("Subsection")
    pdf.add_paragraph("This is a paragraph in a subsection.")
    pdf.save()
