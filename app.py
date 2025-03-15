import pandas as pd
import streamlit as st
import numpy as np

st.title("Prevendo se você teve um bom dia hoje! Responda tudo de 1 até 10")
st.divider()

sono = st.number_input("Digita de 1 até 10 sua Qualidade de Sono hoje")
interacoes = st.number_input("Digita de 1 até 10 quantas Interações Sociais você teve hoje")
resiliencia = st.number_input("Digita de 1 até 10 seu sentimento de Resiliencia hoje")
pertencimento = st.number_input("Digita de 1 até 10 seu sentimento de Pertencimento hoje")

if st.button("Prever"):
        re1 = sono / 30
        re2 = interacoes / 10
        re3 = resiliencia / 20
        re4 = pertencimento / 40
        re5 = re1 + re2 + re3 + re4
        re6 = re5 * 100
        re7 = re6 - 104,5 / 34,872
        result = 0,77696 + 1,2566 * re7
        st.success('Resultado da previsão: {}'.format("Você teve um Bom Dia! (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)" if result >= 0.50 else "Você não teve um bom dia. (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)"))
        print(result)
