import streamlit as st
from controller.controller import ControladorSupermercado
import os


def main(caminho: str) -> None:
    controlador = ControladorSupermercado(caminho)
    controlador.modelo.criar_coluna_mes()
    st.sidebar.markdown(" :balloon: __Nossas opções__ :balloon: ")

    mes_radio = st.sidebar.radio(
        "Mês (Radio Button)", controlador.modelo.df["Mes"].unique()
    )
    st.write(f"Mês selecionado (Radio Button): {mes_radio}")

    mes_selectbox = st.sidebar.selectbox(
        "Mês (Selectbox)", controlador.modelo.df["Mes"].unique()
    )
    st.write(f"Mês selecionado (Selectbox): {mes_selectbox}")

    mes_multiselect = st.sidebar.multiselect(
        "Mês (Multiselect)", controlador.modelo.df["Mes"].unique()
    )
    st.write(f"Mês selecionado (Multiselect): {mes_multiselect}")

    mes_slider = st.sidebar.slider(
        "Mês (Slider)",
        min_value=int(controlador.modelo.df["Date"].dt.month.min()),
        max_value=int(controlador.modelo.df["Date"].dt.month.max()),
        step=1,
    )
    st.write(f"Ano selecionado (Slider): {mes_slider}")

    controlador.executar(mes_radio)


if __name__ == "__main__":
    st.set_page_config(page_title="Exemplo Final", page_icon="😊", layout="wide")
    caminho = os.path.join(os.getcwd(), "assets", "supermarket_sales.csv")
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado em {caminho}")
    main(caminho)
