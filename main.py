from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tarefaslista = []
proximo_id = 1

app = FastAPI()

class Tarefa(BaseModel):
    id : int
    titulo : str
    descricao : str
    concluido : bool
    
@app.get('/')
def ler_raiz():
    return {'Mensagen' : 'Ola mundo'}

@app.get('/tarefas')
def listar_tarefas():
    return tarefaslista

@app.post('/tarefas', status_code=201)
def criar_tarefas(tarefa: Tarefa):
    
    global proximo_id
    
    tarefa.id = proximo_id
    proximo_id += 1
    
    tarefaslista.append(tarefa)
    
    return {"mensagem": "Salvo com sucesso!", "item_salvo": tarefa} 

@app.delete("/tarefas/{id}")
def deletar_tarefas(id: int):
    for tarefa in tarefaslista:
        if tarefa.id == id:
            tarefaslista.remove(tarefa)
            return {"mensagem": f"Tarefa {id} deletada com sucesso!"}
        
    return {"erro": "Tarefa não encontrada"}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, dados: Tarefa):
    for i, tarefa in enumerate(tarefaslista):
        if tarefa.id == tarefa_id:
            dados.id = tarefa_id
            tarefaslista[i] = dados
            return {"mensagem": "Tarefa atualizada com sucesso!", "item_atualizado": dados}

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")