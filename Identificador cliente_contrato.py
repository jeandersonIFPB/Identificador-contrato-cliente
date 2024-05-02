# import packages
import PyPDF2
import re
i = 0
# open the pdf file
reader_1 = PyPDF2.PdfReader("medicao11.pdf")
# get number of pages
# define key terms
#string = "822406"
# extract text and do the search
medicao_str = ""
MARCADOR="CRE D IMOB"

for page1 in reader_1.pages:
    
    medicao_str = medicao_str + (page1.extract_text())
    while (medicao_str.count("CRE D IMOB")):
        posicao1 = medicao_str.find(MARCADOR)
        numero_contrato = (medicao_str[(posicao1-7):(posicao1-1)])
        reader_2 = PyPDF2.PdfReader("clientes.pdf")#abre arquivo clientes

        for page2 in reader_2.pages:
            cliente_str = page2.extract_text()
            if(numero_contrato in cliente_str):
                posicao2 = cliente_str.find(numero_contrato)
                nome_cliente = (cliente_str[(posicao2+7):(posicao2+32)])
                medicao_str = medicao_str.replace(MARCADOR, nome_cliente,1)
print(medicao_str)
with open("Medicao_com_nome_clientes.txt", "w") as arquivo:
	arquivo.write(medicao_str)                
    #res_search = re.search(string, text)
    #print(res_search)
