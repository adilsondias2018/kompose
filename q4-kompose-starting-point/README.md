# Kompose

### Adicione aqui os erros e correções aplicadas


---
**Código com erro:**  
```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",    
    "songs",
]
```
**Erro:** O app "rest_framework" não está declarado em INSTALLED_APPS  
**O que ele causa:** O Django não consegue identificar as informações para fazer as migrations"
**Como corrigir:** Incluir a linha com o nome do app "rest_framework" dentro de INSTALLED_APPS, fazendo com que ele seja reconhecido pelo Django.

```sh
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "songs",
]
```
---

**Código com erro variáveis de ambiente:**  
```sh
DB=kompose
USER=user
PASSWORD=password

```
**Erro:** Faltou acresentar o nome correto no arquivo de variáveis de ambiente. 
**O que ele causa:** A imagem do postgres só reconhece a variáveis com nome incorrento.
**Como corrigir:** Alterar o nome das variáveis com inidicado na documentação.

**Correção do erro:**
```sh
POSTGRES_DB=kompose
POSTGRES_USER=adilson
POSTGRES_PASSWORD=9477

```

**Código com erro no caminho da engine:**  
```sh
 DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgres",
            "NAME": os.getenv("DB"),
            "USER": os.getenv("USER"),
            "PASSWORD": os.getenv("PASSWORD"),
            "HOST": "database",
            "PORT": 5432,
        }
    }



```
**Erro:** Faltou acresentar o camimho correto na engine. 
**O que ele causa:** A engine do postgres não é encontrada e o banco não é iniciado.
**Como corrigir:** Acresentar o caminho correto.

**Correção do erro:**
```sh
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": "db",
            "PORT": 5432,
        }
    }

```


**Código com erro:**  
```python

    FROM python:2.7
    
```
**Erro:** Imagem da versão python 2.7 
**O que ele causa:** A versão foi descontinuada e não faz a atualização dos pacotes.
**Como corrigir:** Atualizar a versão para 3.9

**Correção do erro:**
``` python

FROM python:3.9

```



**Código com erro:**  
```python

        web:
        env_file: envs/dev.env
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py runserver 0.0.0.0:8000'
        
        stdin_open: true
        tty: true
        ports:
            - 8000:8001

        depends_on:
            - db
            - migration

    
```
**Erro:** Trecho desnecessário na docker-compose.
**O que ele causa:** gera conflito na imagem, pois tentar instalar novamente os mesmos pacotes.
**Como corrigir:** Remover trecho do código.

**Correção do erro:**
``` python



```


**Código com erro:**  
```python

       services:
    db:
        image: postgres:latest
        env_file: envs/dev.env
        ports:
            - 5432:5432

    migration:
        build: .
        env_file: envs/dev.env
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py migrate'
        
        stdin_open: true
        tty: true

        depends_on:
            - db

    
```
**Erro:** Faltou informar a pasta ou volume para armazenar os dados do banco na imagem..
**O que ele causa:** Toda vez que a imagem é reiniciada os dados são perdidos.
**Como corrigir:** Acresentar a pasta para armazenar os dados.

**Correção do erro:**
``` python
services:
  db:
    image: postgres:latest
    env_file: envs/dev.env
    ports:
      - 5432:5432
    volumes:
      - pgdata2:/var/lib/postgresql/data


```
==========

**Código com erro:**  
```python

   services:
    db:
        image: postgres:latest
        env_file: envs/dev.env
        ports:
            - 5432:5432

    migration:
        build: .
        env_file: envs/dev.env
        command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py migrate'
        
        stdin_open: true
        tty: true

        depends_on:
            - db



    
```
**Erro:** Faltou informar a pasta ou volume para armazenar os dados na pasta local.
**O que ele causa:** Toda vez que a imagem é reiniciada os dados são perdidos e não são atualizadados na pasta local.
**Como corrigir:** Criar um volume  com o comando docker volume create. Assim tem um copia dos dados na máquina local.

**Correção do erro:**
``` python
version: "3.7"

services:
  db:
    image: postgres:latest
    env_file: envs/dev.env
    ports:
      - 5432:5432
    volumes:
      - pgdata2:/var/lib/postgresql/data

  django_app:
    build: .
    ports:
      - 8005:8001
    command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py runserver 0.0.0.0:8001'
    # command: bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python manage.py migrate'
    entrypoint: ./entrypoint.sh
    stdin_open: true
    tty: true
    volumes:
      - .:/code
    env_file: envs/dev.env
    depends_on:
      - db
volumes:
  pgdata2:
    external: true


```