from model.model import ModeloSupermercado
from view.view import VisualizacaoSupermercado


class ControladorSupermercado:
    def __init__(self, caminho_dados: str):
        self.modelo = ModeloSupermercado(caminho_dados)
        self.visualizacao = VisualizacaoSupermercado()

    def executar(self, mes: str) -> None:
        total_cogs = self.modelo.calcular_total_cogs(mes)
        df_filtrado = self.modelo.obter_dados_por_mes(mes)
        total_do_mes = self.modelo.calcular_total_do_mes(mes)
        margem_de_lucro_bruta = self.modelo.calcular_margem_de_lucro_bruta(mes)
        self.visualizacao.exibir_pagina(
            df_filtrado, total_do_mes, margem_de_lucro_bruta, total_cogs
        )
