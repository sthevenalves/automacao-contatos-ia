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