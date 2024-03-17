import xmltodict as xml
import os 
import pandas as pd

def pegar_arquivos (nome_arquivos, valores):
    print (f"pegou as informaçoes{nome_arquivos}")
    with open(f'nfs/{nome_arquivos}', "rb") as arquivo_xml:
        dic_arquivos = xml.parse (arquivo_xml)
       
      
        if "NFe" in dic_arquivos:
            infos_nf = dic_arquivos ["NFe"]["infNFe"]
        else:
            infos_nf = dic_arquivos["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf ["emit"]["xNome"]
        nome_cliente = infos_nf["dest"]["xNome"]
        endereço = infos_nf["dest"]["enderDest"]
        if "vol" in infos_nf ["transp"]:
            peso = infos_nf ["transp"]["vol"]["pesoB"]
        else:
            peso = "Peso não informado"
        valores.append ([numero_nota, empresa_emissora, nome_cliente, endereço, peso])

arquivos = os.listdir  ("nfs")
colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereço", "peso"]
valores = []

for arquivos in arquivos:
    pegar_arquivos(arquivos, valores)

tabela = pd.DataFrame (columns=colunas , data= valores)
tabela.to_excel ("Notas_Fiscais.xlsx", index= False)