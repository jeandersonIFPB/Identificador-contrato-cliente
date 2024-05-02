# import pacotes
import PyPDF2  
import re
i = 0
reader_1 = PyPDF2.PdfReader("medicao11.pdf") #abre o arquivo pdf
medicao_str = "" #String que irá receber string do pdf
MARCADOR="CRE D IMOB" #Marcador para identificar a linha dos clientes
 
for page1 in reader_1.pages:
    
    medicao_str = medicao_str + (page1.extract_text()) #Extrai string de uma página e concatena com a próxima
    while (medicao_str.count("CRE D IMOB")): #Enquanto houver a string CRE D IMOB faça:
        posicao1 = medicao_str.find(MARCADOR) #extrai posição do primeiro caractere do marcador CRE D IMOB
        numero_contrato = (medicao_str[(posicao1-7):(posicao1-1)]) #Por meio da posição do marcador extrai o numero do contrato
        reader_2 = PyPDF2.PdfReader("clientes.pdf")#abre arquivo clientes 

        for page2 in reader_2.pages: #Faz loop página por página no arquivo clientes
            cliente_str = page2.extract_text() #extrai texto do arquivo com nome dos clientes
            if(numero_contrato in cliente_str):# se há número do contrato no arquivo clientes
                posicao2 = cliente_str.find(numero_contrato) #busca posição do número do contrato no cliente
                nome_cliente = (cliente_str[(posicao2+7):(posicao2+32)])# Por meio da posição do número do contrato extrai os 25 caracteres do nome do cliente
                medicao_str = medicao_str.replace(MARCADOR, nome_cliente,1) #Substitui marcador no arquivo medição pelo nome do cliente
with open("Medicao_com_nome_clientes.txt", "w") as arquivo:#Cria novo arquivo medicao com todos os clientes já identificados
	arquivo.write(medicao_str)                
    #res_search = re.search(string, text)
    #print(res_search)
