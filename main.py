import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

#CONFIGURAÇÃO 

API_KEY = "SUA_CHAVE_API_AQUI"

INPUT_FILE = "sites.txt"
OUTPUT_FILE = "resultado_telefones.csv"

MODELO = "gpt-4o-mini"


client = OpenAI(api_key=API_KEY)

def limpar_html(html_content):
    """
    Usa BeautifulSoup para remover scripts, estilos e tags desnecessárias,
    retornando apenas o texto visível para economizar tokens.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    if len(soup.text) > 2000:
        for element in soup([
            "script", "style", "meta", "noscript",
            "header", "svg", "path"
        ]):
            element.extract()

    return soup

def extrair_telefone_com_ia(texto_site, url):
    """
    Envia o texto do site para a OpenAI identificar o telefone.
    """
    prompt_sistema = (
        "Você é um assistente especialista em extração de dados. "
        "Sua tarefa é encontrar o número de telefone principal de contato comercial no código HTML fornecido de um site. "
        "Se houver vários, prefira celulares (WhatsApp) ou fixos locais. Pesquise dentro dos links (parâmetros href das tags a do html se existe um numero de telefone também, ele pode estar em um parâmetro no link chamado phone= ou algo parecido)"
        "Retorne APENAS o número formatado. Se não encontrar, retorne 'Não encontrado'."
    )

    prompt_usuario = f"URL do site: {url}\n\nConteúdo do site:\n{texto_site}\n\nExtraia o telefone:"

    try:
        response = client.chat.completions.create(
            model=MODELO,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro na IA: {e}"