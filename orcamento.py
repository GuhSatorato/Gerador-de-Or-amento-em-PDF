from fpdf import FPDF

projeto = input("Qual a descrição do projeto: ")
horas_estimada = input("Quantas horas estimada para o projeto: ")
valor_hora = input("Quanto irá ser cobrado por hora do projeto: ")
prazo = input("Qual o prazo estimado para o fim do projeto: ")

valor_total = float(horas_estimada) * float(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimada)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")