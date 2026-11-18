import json
import webview
import os

class Api_Selector:
    def __init__(self):
        pass

    def selecionar_relatorio():
        ...

class Api:
    def __init__(self):
        pass

    def selecionar_arquivo():
        pass

    def processar_arquivo():
        pass
    

caso = 0

base = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(base, "pages" ,"index.html")
caminho_minitela = os.path.join(base, "pages", "selector.html")

api_selec = Api_Selector()
window = webview.create_window(
    "Relatório de retorno v1.0", caminho_minitela, js_api=api_selec, width=400, height=300
)
webview.start()

match caso:

    case 0:

        api = Api()
        window = webview.create_window(
            "Relatório de retorno v1.0 (MOVEL)", caminho, js_api=api, width=700, height=700
        )
        webview.start()

    case 1:
        api = Api()
        window = webview.create_window(
            "Relatório de retorno v1.0 (FIXA NAC)", caminho, js_api=api, width=700, height=700
        )
        webview.start()

    case 2:
        api = Api()
        window = webview.create_window(
            "Relatório de retorno v1.0 (FIXA REG)", caminho, js_api=api, width=700, height=700
        )
        webview.start()



