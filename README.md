
<div align="center">

# 🖥️ Monitoramento de Arquivos

### Sistema de Monitoramento de Alterações com Python e Django

**Aplicação web para acompanhamento de arquivos e visualização de registros de atualização.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Watchdog](https://img.shields.io/badge/Watchdog-334155?style=for-the-badge)

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias-utilizadas) •
[Instalação](#-instalação-e-execução) •
[Estrutura](#-estrutura-do-projeto)

</div>

---

## 📖 Sobre o projeto

O **Monitoramento de Arquivos** é um projeto acadêmico desenvolvido em Python com o framework Django, voltado ao acompanhamento de modificações em arquivos de um diretório.

A aplicação combina o monitoramento de eventos do sistema de arquivos com o armazenamento de informações em um banco de dados SQLite e sua apresentação em uma interface web.

O projeto utiliza a biblioteca **Watchdog** para observar eventos de modificação e o **Django** para gerenciar os registros e disponibilizar as informações por meio de uma aplicação web.

### 🎯 Objetivos

- Estudar o monitoramento de arquivos com Python.
- Identificar eventos de modificação no sistema de arquivos.
- Integrar processos de monitoramento ao Django.
- Armazenar informações em um banco de dados.
- Desenvolver uma interface web para consulta dos registros.
- Aplicar conceitos de automação e desenvolvimento web.

---

## ✨ Funcionalidades

### 📂 Monitoramento de arquivos

O módulo de monitoramento foi desenvolvido com a biblioteca Watchdog.

Entre os recursos implementados no código estão:

- Observação de eventos de modificação em arquivos.
- Identificação do nome e caminho do arquivo modificado.
- Filtragem dos arquivos monitorados.
- Registro de eventos por meio da biblioteca `logging`.
- Integração com os modelos do Django.

### 💾 Persistência de dados

O projeto utiliza SQLite para armazenar informações sobre os arquivos monitorados.

O modelo `File` possui os seguintes campos:

| Campo | Descrição |
|:---|:---|
| `id` | Identificador do registro |
| `name` | Nome do arquivo |
| `path` | Caminho do arquivo |
| `updated_at` | Data e horário da atualização |

A aplicação utiliza o método `update_or_create()` do Django para criar ou atualizar registros de arquivos identificados pelo monitoramento.

### 🌐 Interface web

O sistema possui uma página de gerenciamento com:

- Listagem dos arquivos registrados.
- Exibição do nome de cada arquivo.
- Apresentação da data e hora de atualização.
- Mensagem informativa quando não existem registros.
- Indicador durante o carregamento.
- Tratamento visual de erros de consulta.

### 🔄 Atualização periódica

A interface utiliza JavaScript e a Fetch API para consultar os registros.

O navegador realiza novas requisições ao servidor a cada **5 segundos**, atualizando a listagem sem necessidade de recarregar a página inteira.

> **Estado da implementação:** a interface e a consulta ao banco estão implementadas, mas o script de monitoramento precisa de correções para executar corretamente. A atualização da página utiliza consultas periódicas, não WebSockets.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|:---|:---|
| **Python** | Linguagem principal |
| **Django 3.2** | Framework web e gerenciamento da aplicação |
| **SQLite** | Armazenamento dos registros |
| **Watchdog** | Monitoramento de eventos do sistema de arquivos |
| **HTML5** | Estrutura da interface |
| **CSS3** | Estilização da página |
| **JavaScript** | Atualização dinâmica da listagem |
| **Fetch API** | Comunicação HTTP com o servidor |

### Bibliotecas Python

O projeto também utiliza módulos da biblioteca padrão:

- `os`: manipulação de caminhos e diretórios.
- `sys`: configuração de caminhos de importação.
- `time`: controle do ciclo de execução.
- `logging`: registro de eventos e erros.

---

## 🏗️ Arquitetura do sistema

A aplicação é dividida em três componentes principais:

1. **Monitoramento:** observa alterações no sistema de arquivos.
2. **Persistência:** armazena os registros utilizando Django ORM e SQLite.
3. **Interface:** consulta e apresenta os registros por meio de requisições HTTP.

```text
                ┌─────────────────────┐
                │ SISTEMA DE ARQUIVOS │
                │ Diretório observado │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      WATCHDOG       │
                │ Eventos de alteração│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     DJANGO ORM      │
                │ Gerenciamento File  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       SQLite        │
                │ Registros de arquivo│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     DJANGO WEB      │
                │ Endpoint JSON       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     INTERFACE       │
                │    HTML/CSS/JS      │
                └─────────────────────┘
```

O diagrama representa a arquitetura proposta. O fluxo completo depende das correções indicadas na seção de limitações.

---

## 📁 Estrutura do projeto

```text
Monitoramento/
│
├── Monitoramento_arquivos/
│   │
│   ├── App/
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   └── 0002_auto_20250226_0111.py
│   │   │
│   │   ├── templates/
│   │   │   └── home.html
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── monitoramento.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── Monitor/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│   └── teste.txt
│
└── README.md
```

### Principais arquivos

| Arquivo | Responsabilidade |
|:---|:---|
| `manage.py` | Gerenciamento da aplicação Django |
| `settings.py` | Configurações do projeto |
| `models.py` | Definição do modelo de arquivos |
| `views.py` | Renderização da página e retorno dos dados |
| `monitoramento.py` | Observação das alterações nos arquivos |
| `home.html` | Interface de visualização dos registros |
| `db.sqlite3` | Banco de dados SQLite |

---

## 🚀 Instalação e execução

### Pré-requisitos

- Python instalado.
- pip para gerenciamento de dependências.
- Git para clonar o repositório.

> O projeto foi gerado com Django 3.2.25. Para reproduzir o ambiente original, utilize Python 3.7 a 3.10, preferencialmente em um ambiente isolado. Essa versão do Django já está fora do período de suporte de segurança.

### 1. Clone o repositório

```bash
git clone https://github.com/JuliaGabrielyPereiraRodrigues/Monitoramento.git
```

Acesse a pasta da aplicação:

```bash
cd Monitoramento/Monitoramento_arquivos
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual.

**Windows:**

```powershell
.\venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install "Django==3.2.25" watchdog
```

### 4. Prepare o banco de dados

Execute as migrações:

```bash
python manage.py migrate
```

O Django utilizará o banco SQLite configurado no projeto.

### 5. Inicie o servidor web

```bash
python manage.py runserver
```

Acesse:

**http://127.0.0.1:8000/**

A página exibirá os registros existentes no banco de dados e realizará consultas periódicas para atualizar a listagem.

### 6. Monitoramento de arquivos

O script responsável pelo monitoramento está localizado em:

```text
App/monitoramento.py
```

Sua execução prevista é:

```bash
python App/monitoramento.py
```

**Atenção:** antes de utilizar esse comando, é necessário corrigir a inicialização da lista `target_files`, criar o diretório observado e ajustar a comparação dos caminhos dos arquivos.

Sem essas alterações, o monitoramento não funciona corretamente.

---

## 🔗 Rotas da aplicação

| Método | Rota | Descrição |
|:---|:---|:---|
| `GET` | `/` | Exibe a interface principal |
| `GET` | `/get-files/` | Retorna a lista de arquivos em JSON |
| `GET` | `/admin/` | Acesso à administração do Django |

### Exemplo de resposta

O endpoint `/get-files/` retorna registros no seguinte formato:

```json
[
  {
    "name": "exemplo.txt",
    "path": "/diretorio/exemplo.txt",
    "updated_at": "2025-02-26T01:11:00Z"
  }
]
```

O exemplo ilustra a estrutura JSON. Os valores dependem dos registros armazenados no banco.


---

## 📚 Aprendizados

O projeto permite explorar conhecimentos em:

- Programação Python.
- Desenvolvimento web com Django.
- Organização de projetos no padrão MVT.
- Modelagem de dados com Django ORM.
- Persistência de informações com SQLite.
- Monitoramento de eventos do sistema de arquivos.
- Integração entre processos Python e aplicações web.
- Requisições HTTP e respostas JSON.
- Atualização dinâmica de interfaces com JavaScript.
- Registro e tratamento de erros.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido para fins educacionais, com foco na integração entre automação de tarefas, monitoramento de arquivos, persistência de dados e desenvolvimento web utilizando Python.

---

## 👩‍💻 Autoria

Desenvolvido por **[Julia Gabriely](https://github.com/JuliaGabrielyPereiraRodrigues)**.

<div align="center">

---

**[⬆ Voltar ao topo](#️-monitoramento-de-arquivos)**

</div>
