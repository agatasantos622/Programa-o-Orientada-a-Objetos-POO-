import streamlit as st
from imovel import Apartamento, Casa, Estudio
from contrato import Contrato
from gerador_csv import gerar_csv

st.set_page_config(page_title="Orçamento Imobiliária R.M", layout="centered")

st.title("🏠 Orçamento Imobiliária R.M")
st.write("Selecione as opções abaixo para gerar o orçamento do imóvel.")

tipo = st.selectbox("Tipo de imóvel", ["Apartamento", "Casa", "Estúdio"])

imovel = None

if tipo == "Apartamento":
    quartos = st.selectbox("Quantidade de quartos", [1, 2])
    garagem = st.checkbox("Possui garagem")
    crianca = st.radio("Possui crianças?", ["Sim", "Não"]) == "Sim"
    imovel = Apartamento(quartos, garagem, crianca)

elif tipo == "Casa":
    quartos = st.selectbox("Quantidade de quartos", [1, 2])
    garagem = st.checkbox("Possui garagem")
    imovel = Casa(quartos, garagem)

elif tipo == "Estúdio":
    vagas = st.number_input("Quantidade de vagas de estacionamento", min_value=0, step=1)
    imovel = Estudio(vagas)

st.divider()

parcelas = st.slider("Parcelas do contrato (até 5x)", min_value=1, max_value=5, value=1)
contrato = Contrato()
valor_parcela = contrato.parcelar(parcelas)
parcelas_final = parcelas


if st.button("💰 Gerar Orçamento"):
    valor_aluguel = imovel.calcular_valor()

    st.subheader("📊 Resultado do Orçamento")
    st.write(f"**Tipo do imóvel:** {imovel.tipo}")
    st.write(f"**Valor do aluguel mensal:** R$ {valor_aluguel:.2f}")
    st.write(f"**Contrato:** R$ 2.000,00 em {parcelas_final}x de R$ {valor_parcela:.2f}")

    gerar_csv(valor_aluguel)

    st.success("Arquivo 'parcelas_orcamento.csv' gerado com sucesso!")
    st.caption("O arquivo foi salvo na pasta do projeto.")

st.divider()
st.caption("Aplicação desenvolvida em Python com Streamlit – Projeto acadêmico")

