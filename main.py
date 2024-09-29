from fastapi import FastAPI
#from pydantic import BaseModel
from DataBase.DataBase import RegisterDB

from Lancamento.LancamentoService import LancamentoService

from Lancamento.LancamentoController import LancamentoController

registerDB = RegisterDB()

app = FastAPI()

lancamentoService = LancamentoService(registerDB)

LancamentoController(app, lancamentoService)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
