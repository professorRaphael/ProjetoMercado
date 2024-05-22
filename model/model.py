import pandas as pd


class ModeloSupermercado:
    def __init__(self, caminho_dados: str):
        try:
            self.df = pd.read_csv(caminho_dados, sep=";", decimal=",", thousands=".")
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado em {caminho_dados}")
        except pd.errors.ParserError:
            raise ValueError(f"Erro ao processar o arquivo {caminho_dados}")
        self.df["Date"] = pd.to_datetime(self.df["Date"], errors="coerce")
        self.df = self.df.dropna(subset=["Date"])
        self.df = self.df.sort_values("Date")

    def criar_coluna_mes(self) -> None:
        self.df["Mes"] = self.df["Date"].dt.strftime("%Y-%m")

    def obter_dados_por_mes(self, mes: str) -> pd.DataFrame:
        return self.df[self.df["Mes"] == mes]

    def calcular_total_do_mes(self, mes: str, coluna_alvo: str = "Total") -> float:
        df_mes = self.obter_dados_por_mes(mes)
        total_mes = df_mes[coluna_alvo].sum()
        return total_mes

    def calcular_total_cogs(self, mes: str) -> float:
        df_mes = self.obter_dados_por_mes(mes)
        total_cogs = df_mes["cogs"].sum()
        return total_cogs

    def calcular_margem_de_lucro_bruta(self, mes: str) -> float:
        total_do_mes = self.calcular_total_do_mes(mes)
        total_cogs = self.calcular_total_cogs(mes)
        if total_do_mes == 0:
            return 0.0
        margem_de_lucro_bruta = ((total_do_mes - total_cogs) / total_do_mes) * 100
        return margem_de_lucro_bruta
