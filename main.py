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
    """
Lista todas as tarefas registradas.

Args:
    sem args.

Returns:
    retorna a lista das tarefas.
    """
    
    return tarefaslista

@app.post('/tarefas', status_code=201)
def criar_tarefas(tarefa: Tarefa):
    """
Cria uma nova tarefas.

Args:
    tarefa (Tarefa): a classe usada para criar uma nova tarefa, o 'placeholder'

Returns:
    retorna uma mensagem de comfirmaçao + a tarefa em si.
    """
    
    #Global temporario, unicamente para testes, sera corrigido para sistema de classes/POO
    global proximo_id
    
    tarefa.id = proximo_id
    proximo_id += 1
    
    tarefaslista.append(tarefa)
    
    return {"mensagem": "Salvo com sucesso!", "item_salvo": tarefa} 

@app.delete("/tarefas/{id}")
def deletar_tarefas(id: int):
    """
deleta tarefas ativas.

Args:
    id (int): numero de identificaçao (ID) da tarefa a ser deletada.

Returns:
    retorna uma mensagem de sucesso ou erro.
    """
    for tarefa in tarefaslista:
        if tarefa.id == id:
            tarefaslista.remove(tarefa)
            return {"mensagem": f"Tarefa {id} deletada com sucesso!"}
        
    return {"erro": "Tarefa não encontrada"}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, dados: Tarefa):
    """
Atualiza as informaçoes de uma tarefa.

Args:
    tarefa_id (int): Identifica a tarefa
    dados (Tarefa): quais novas informaçoes a tarefa recebera

Returns:
    retorna uma mensagen de sucesso ou erro.
    """
    for i, tarefa in enumerate(tarefaslista):
        if tarefa.id == tarefa_id:
            dados.id = tarefa_id
            tarefaslista[i] = dados
            return {"mensagem": "Tarefa atualizada com sucesso!", "item_atualizado": dados}

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")