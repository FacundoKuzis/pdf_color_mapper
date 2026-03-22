from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

pdf = PDF()
pdf.add_page()
pdf.set_margins(20, 20, 20)
pdf.set_auto_page_break(auto=True, margin=20)

def section(title):
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, title, ln=True)
    pdf.set_draw_color(180, 180, 180)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(4)

def body(text):
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 6, text)
    pdf.ln(2)

def step(n, title, desc):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(6, 6, f'{n}.', ln=False)
    pdf.cell(0, 6, title, ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(26)
    pdf.multi_cell(0, 6, desc)
    pdf.ln(1)

def label_row(label, desc):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, label, ln=True)
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(26)
    pdf.multi_cell(0, 6, desc)
    pdf.ln(1)

# Título
pdf.set_font('Helvetica', 'B', 20)
pdf.set_text_color(0, 0, 0)
pdf.ln(4)
pdf.cell(0, 11, 'PDF / Image Color Mapper', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(90, 90, 90)
pdf.cell(0, 7, 'Cómo funciona y cómo usarlo', ln=True)
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.5)
pdf.line(20, pdf.get_y() + 3, 190, pdf.get_y() + 3)

# ── QUÉ HACE ──
section('Qué hace')
body(
    'Esta herramienta toma un archivo PDF, PNG o JPG y reemplaza sus colores según el mapeo '
    'que vos definás. La lógica funciona así: cada píxel de la imagen se analiza según su '
    'luminosidad. Los píxeles claros (cercanos al blanco) se reemplazan por el color "destino '
    'claro", y los píxeles oscuros (cercanos al negro) se reemplazan por el color "destino oscuro". '
    'Los tonos intermedios reciben una mezcla proporcional entre ambos, logrando una transición '
    'suave y sin bordes duros.\n\n'
    'En el caso de los PDF, cada página se convierte a imagen y luego se reensambla en un PDF '
    'nuevo. Esto significa que el texto del PDF original no será seleccionable en el archivo final.'
)

# ── CÓMO USARLO ──
section('Cómo usarlo paso a paso')
step('1', 'Cargar un archivo',
    'Hacé clic en el campo "Archivo" y seleccioná un PDF, PNG o JPG desde tu computadora.')
step('2', 'Elegir una combinación de colores',
    'Hay más de 40 combinaciones predefinidas disponibles (por ejemplo: "Oro oscuro", "Sepia", '
    '"Azul marino", etc.). Cada una aplica automáticamente un esquema de colores distinto para '
    'el fondo y el texto. Basta con hacer clic en la que más te guste para aplicarla, y el '
    'resultado se actualiza solo en la vista previa.')
step('3', 'Revisar el resultado',
    'La vista previa de la derecha muestra cómo quedará el archivo con los colores elegidos. '
    'Si el archivo es un PDF de varias páginas, podés navegar con los botones "Anterior" y "Siguiente".')
step('4', 'Descargar',
    'Cuando el resultado te convenza, escribí el nombre del archivo de salida y presioná '
    '"Descargar archivo". El archivo se guardará en tu carpeta de descargas.')

# ── COLORES PERSONALIZADOS ──
section('Configuración de colores personalizada')
body(
    'Al final del panel de controles encontrás cuatro selectores de color. Ahí podés definir '
    'exactamente qué color querés para el fondo y para el texto, sin depender de las combinaciones predefinidas.'
)
body('Los cuatro campos que podés configurar son:')

label_row('Color claro origen:',
    'El color que la herramienta va a detectar como "blanco" en tu archivo. Por defecto es blanco puro (#ffffff).')
label_row('Destino del claro:',
    'A qué color se va a reemplazar ese blanco. Si querés fondo negro, poné #000000 acá.')
label_row('Color oscuro origen:',
    'El color que la herramienta va a detectar como "negro". Por defecto es negro puro (#000000).')
label_row('Destino del oscuro:',
    'A qué color se va a reemplazar ese negro. Si querés texto blanco, poné #ffffff acá.')

pdf.ln(2)
body(
    'Ejemplo práctico: si querés que el PDF tenga fondo negro con texto blanco, configurá '
    '"Destino del claro" en #000000 y "Destino del oscuro" en #ffffff. '
    'La vista previa se actualizará automáticamente para que puedas verificar el resultado.'
)

pdf.output('/workspaces/pdf_color_mapper/color_mapper_guia.pdf')
print('PDF generado.')
