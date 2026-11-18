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