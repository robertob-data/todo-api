# Todo API

API simples de gerenciamento de tarefas (CRUD) construída com FastAPI, como projeto de estudo/portfólio.

## Funcionalidades

- Listar tarefas
- Criar tarefa
- Atualizar tarefa
- Deletar tarefa

## Tecnologias

- Python
- FastAPI
- Pydantic

## Como rodar

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Acesse a documentação interativa em `http://127.0.0.1:8000/docs`

## Endpoints

| Método | Rota            | Descrição                  |
|--------|-----------------|-----------------------------|
| GET    | /tarefas        | Lista todas as tarefas      |
| POST   | /tarefas        | Cria uma nova tarefa        |
| PUT    | /tarefas/{id}   | Atualiza uma tarefa         |
| DELETE | /tarefas/{id}   | Deleta uma tarefa           |

## Status do projeto

Em desenvolvimento — dados armazenados em memória (sem persistência ainda). 

**Próximos passos:**
- Migrar armazenamento para banco de dados (SQLite)
- Refatorar geração de ID (atualmente usa `global` como solução temporária)
- Adicionar autenticação
