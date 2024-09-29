


class LancamentoController:
    def __init__(self, app, lancamentoService):

        @app.get("/lancamento")
        async def getLancamento():            
            name = "Davi"
            return await lancamentoService.getLancamento(name)
        