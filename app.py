import pandas as pd 
import streamlit as st
import numpy as np

def welcome():
    st.title("Prevendo se você teve um bom dia hoje! Responda tudo de 1 até 10")
    st.divider()

def main():
    sono = st.number_input("Digite de 1 até 10 sua Qualidade de Sono hoje", min_value=1, max_value=10, step=1)
    interacoes = st.number_input("Digite de 1 até 10 quantas Interações Sociais você teve hoje", min_value=1, max_value=10, step=1)
    resiliencia = st.number_input("Digite de 1 até 10 seu sentimento de Resiliência hoje", min_value=1, max_value=10, step=1)
    pertencimento = st.number_input("Digite de 1 até 10 seu sentimento de Pertencimento hoje", min_value=1, max_value=10, step=1)

    peso_sono = 30
    peso_interacoes = 10
    peso_resiliencia = 20
    peso_pertencimento = 40

    if st.button("Prever"):
        re1 = sono / peso_sono  # Sono com peso 30
        re2 = interacoes / peso_interacoes  # Interações Sociais com peso 10
        re3 = resiliencia / peso_resiliencia  # Resiliência com peso 20
        re4 = pertencimento / peso_pertencimento  # Pertencimento com peso 40
        re5 = re1 + re2 + re3 + re4

        re6 = re5 * 100
        re7 = re6 - 104.5
        re8 = re7 / 34.872
        zscore = 0.77696 + 1.2566 * re8

        st.write("re1 (Sono ponderado):", re1)
        st.write("re2 (Interações ponderado):", re2)
        st.write("re3 (Resiliência ponderado):", re3)
        st.write("re4 (Pertencimento ponderado):", re4)
        st.write("re5 (Soma ponderada):", re5)
        st.write("re6 (Ajuste de escala):", re6)
        st.write("re7 (Ajuste final):", re7)
        st.write("re8 (Normalização final):", re8)
        st.write("zscore:", zscore)

        result = 1 / ((1 + np.exp(-(-zscore))))

        st.write("Resultado da fórmula de regressão logística:", result)

        if result >= 0.5:
            st.success('Resultado da previsão: Você teve um Bom Dia! (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)')
        else:
            st.success('Resultado da previsão: Você não teve um bom dia. (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)')

        print(result)

if __name__ == '__main__':
    welcome()
    main()
