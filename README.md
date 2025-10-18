# 🚀 Projeto Sprint 1: Pipeline ETL de Dados da COVID-19 (SRAG)

Este projeto representa o entregável final da **Sprint 1** do Bootcamp Intensivo de Engenharia de Dados. O objetivo foi construir um pipeline ETL (Extração, Transformação e Carga) completo e funcional em um ambiente local, demonstrando a capacidade de orquestrar diferentes tecnologias para mover e tratar dados do mundo real.

O pipeline extrai dados públicos sobre Síndrome Respiratória Aguda Grave (SRAG) da plataforma Kaggle, realiza um processo de limpeza e transformação de tipos de dados em memória utilizando PySpark e, por fim, carrega o dataset tratado em um banco de dados SQL Server para consumo analítico.

## 🔧 Stack Técnica

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" height="40" alt="jupyter logo"  />
  <img src="https://www.vectorlogo.zone/logos/apache_spark/apache_spark-icon.svg" height="40" alt="spark logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/microsoftsqlserver/microsoftsqlserver-plain-wordmark.svg" height="40" alt="mssql logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/anaconda/anaconda-original.svg" height="40" alt="anaconda logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kaggle/kaggle-original.svg" height="40" alt="kaggle logo"  />
</div>

-   **Linguagem:** Python 3.9
-   **Ambiente:** Anaconda (com ambiente virtual `anaconda-etl`)
-   **Processamento de Dados:** Apache Spark (via PySpark)
-   **Dependência Core:** Java (OpenJDK 17)
-   **Banco de Dados:** Microsoft SQL Server 2022 Express Edition
-   **Ferramenta de SGBD:** SQL Server Management Studio (SSMS)
-   **Aquisição de Dados:** Kaggle API
-   **Conectividade:** Microsoft JDBC Driver for SQL Server


## ⚙️ Configuração do Ambiente

Siga os passos abaixo para replicar o ambiente e executar o projeto.

### 1. Pré-requisitos
-   Git instalado.
-   Anaconda Distribution instalado.
-   SQL Server 2022 Express e SSMS instalados.

### 2. Clonar o Repositório
```bash
git clone [https://github.com/wallace-pv/Sprint1-ETL-SRAG.git]
cd Bootcamp-Sprint1
```

### 3. Configurar o Banco de Dados (SQL Server)
-   **Habilitar Conexões de Rede:** Habilite o serviço **SQL Server Browser** e o protocolo **TCP/IP** no SQL Server Configuration Manager.
-   **Criar o Banco:** Abra o SSMS, conecte-se à sua instância e execute o script `sql/create_database.sql` para criar o banco de dados `datalake_local`.

### 4. Configurar o Ambiente de Processamento (Java e Python)
-   **Instalar Java (JDK 17):**
    -   O PySpark requer Java para funcionar. Baixe e instale o **OpenJDK 17 (LTS)** do [Eclipse Adoptium](https://adoptium.net/).
    -   Durante a instalação, na tela de "Custom Setup", **habilite a opção para configurar a variável de ambiente `JAVA_HOME` automaticamente**.

-   **Criar Ambiente Python Isolado:**
    -   Abra o **Anaconda Prompt**.
    -   Crie e ative o ambiente virtual:
        ```bash
        conda create --name anaconda-etl python=3.9 -y
        conda activate anaconda-etl
        ```
    -   Instale as dependências necessárias (PySpark, Jupyter e Kaggle):
        ```bash
        conda install -c conda-forge pyspark jupyter -y
        pip install kaggle
        ```

### 5. Configurar Segredos e Conectores
-   **API do Kaggle:** Baixe seu token `kaggle.json` do site do Kaggle e coloque-o em `C:\Users\<Seu-Usuario>\.kaggle\`.
-   **Driver JDBC:** Baixe o [Microsoft JDBC Driver for SQL Server](https://learn.microsoft.com/pt-br/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server) e mova o arquivo `.jar` para a pasta `drivers/`.
-   **Senha do Banco:** Crie um arquivo `config.ini` na raiz do projeto (conforme o exemplo no notebook) e preencha com suas credenciais do SQL Server. Este arquivo já está no `.gitignore`.

## ▶️ Como Executar o Pipeline

1.  Abra o **Anaconda Prompt** e ative o ambiente: `conda activate anaconda-etl`.
2.  Navegue até a pasta do projeto e inicie o Jupyter: `jupyter notebook`.
3.  Abra o notebook localizado em `notebooks/validacao_spark.ipynb`.
4.  Execute todas as células de cima para baixo.
5.  Ao final, valide no **SSMS** se a tabela `dbo.casos_srag_tratados` foi criada e populada no banco `datalake_local`.

## 🧠 Desafios Superados e Lições Aprendidas

A implementação deste pipeline foi uma jornada de depuração que revelou desafios práticos cruciais:
-   **Incompatibilidade de Ambiente:** O PySpark exigiu uma versão específica do **Java (JDK 17)**, gerando um erro `UnsupportedClassVersionError` que foi resolvido alinhando as versões.
-   **Configuração de Rede do SQL Server:** A conexão JDBC falhou inicialmente devido ao serviço **SQL Server Browser** estar desativado e o protocolo **TCP/IP** não estar habilitado por padrão.
-   **Qualidade dos Dados de Origem:** A maior dificuldade foi lidar com a inconsistência dos dados no arquivo CSV, que continha múltiplos formatos de data, espaços em branco ocultos, codificação não-padrão e linhas estruturalmente corrompidas.
-   **Segurança:** Credenciais foram removidas do código e migradas para um arquivo `config.ini`, que é ignorado pelo Git, seguindo as melhores práticas de segurança.

