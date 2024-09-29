
class LancamentoService:
    def __init__(self, registerDB):
        self.registerDB = registerDB

    async def getLancamento(self, name: str):
        query = "SELECT * FROM lancamento"
        lancamentos = self.registerDB.query(query)
        print(lancamentos)
        colunas = ["id", "ticket", "nome", "quantidade", "preco", "data", "compra"]

        lancamentos_dict = [
            {colunas[i]: lancamento[i] for i in range(len(colunas))}
            for lancamento in lancamentos
        ]
        return lancamentos_dict
    