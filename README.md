# Automação de Extração de Telefones com IA

Projeto desenvolvido em Python para automatizar a coleta de números de telefone de contato em sites, combinando **web scraping** com **inteligência artificial (OpenAI)** para identificar informações relevantes no conteúdo das páginas.

## Sobre o projeto

A aplicação recebe uma lista de URLs, acessa cada site, extrai seu conteúdo HTML e utiliza a IA para identificar o principal telefone de contato comercial. Ao final do processamento, os resultados são armazenados em um arquivo CSV, facilitando a organização e utilização dos dados coletados.

O projeto busca simplificar a coleta de informações de contato, reduzindo o trabalho manual e explorando o uso de IA na automação de tarefas de extração de dados.

## Funcionalidades

- Leitura de URLs a partir de um arquivo de texto.
- Acesso automatizado a sites utilizando HTTP requests.
- Processamento e limpeza do HTML com BeautifulSoup.
- Remoção de elementos desnecessários para reduzir o conteúdo enviado à IA.
- Extração de telefones utilizando a API da OpenAI.
- Tratamento de erros de conexão e falhas durante o processamento.
- Exportação dos resultados para um arquivo CSV.

## Tecnologias utilizadas

- **Python**
- **Requests** – Requisições HTTP para acessar os sites.
- **BeautifulSoup4** – Parsing e processamento de HTML.
- **OpenAI API** – Identificação e extração de telefones utilizando IA.

## Estrutura do projeto

```text
automacao-contatos-ia/
│
├── main.py
├── sites.txt
├── requirements.txt
└── resultado_telefones.csv
```

| Arquivo | Descrição |
|---|---|
| `main.py` | Código principal da automação |
| `sites.txt` | Lista de sites que serão processados |
| `requirements.txt` | Dependências do projeto |
| `resultado_telefones.csv` | Arquivo gerado com os telefones extraídos |

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/sthevenalves/automacao-contatos-ia.git
```

### 2. Acesse a pasta do projeto

```bash
cd automacao-contatos-ia
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure sua chave da OpenAI

No arquivo `main.py`, configure sua chave de API da OpenAI na variável `API_KEY`.

```python
API_KEY = "SUA_CHAVE_API_AQUI"
```

### 6. Adicione os sites

Insira as URLs que deseja processar no arquivo `sites.txt`, colocando um site por linha.

```text
https://www.exemplo.com.br
https://www.outrosite.com.br
```

O programa também aceita domínios sem o prefixo `https://`.

### 7. Execute a aplicação

```bash
python main.py
```

Após a execução, os resultados serão armazenados no arquivo `resultado_telefones.csv`.

## Exemplo de resultado

O arquivo CSV gerado possui a seguinte estrutura:

| URL | Telefone Extraído |
|---|---|
| https://www.exemplo.com.br | (42) 3333-3333 |
| https://www.outrosite.com.br | (11) 99999-9999 |

Caso não seja identificado um telefone, a IA retorna `Não encontrado`. Problemas de acesso aos sites também são registrados no arquivo de saída.

## Fluxo da aplicação

graph TD

    A["sites.txt - Lista de URLs"] --> B["Leitura dos sites"]
    B --> C["Requisição HTTP com Requests"]
    C --> D["Limpeza do HTML com BeautifulSoup"]
    D --> E["Envio do conteúdo para OpenAI"]
    E --> F["Identificação do telefone"]
    F --> G["Geração do resultado"]
    G --> H["Salvamento no CSV"]

Etapas do processamento:

    Entrada: leitura das URLs armazenadas em sites.txt.
    
    Requisição: acesso aos sites utilizando Requests.
    
    Tratamento: limpeza do HTML com BeautifulSoup.
    
    Extração: envio do conteúdo para a OpenAI identificar o telefone.
    
    Resultado: identificação do telefone ou registro de uma falha.
    
    Exportação: armazenamento dos resultados em resultado_telefones.csv.

## Aprendizados

Durante o desenvolvimento, foram explorados conceitos de:

- Web scraping e requisições HTTP.
- Manipulação e parsing de HTML.
- Integração com APIs de inteligência artificial.
- Automação de processos de coleta de dados.
- Tratamento de exceções e erros de comunicação.
- Manipulação e exportação de arquivos CSV.

## Melhorias futuras

- Utilizar variáveis de ambiente para armazenar a chave da API.
- Implementar logs para acompanhar o processamento.
- Melhorar a validação e padronização dos números extraídos.
- Implementar processamento paralelo para múltiplos sites.
- Criar uma interface para facilitar a utilização da ferramenta.

---

Projeto desenvolvido para fins de aprendizado e exploração de automação de coleta de dados com Python e inteligência artificial.
