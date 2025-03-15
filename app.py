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

    if st.button("Prever"):
        re1 = sono / 30
        re2 = interacoes / 10
        re3 = resiliencia / 20
        re4 = pertencimento / 40
        re5 = re1 + re2 + re3 + re4
        re6 = re5 * 100
        re7 = re6 - 104.5 
        re8 = re7 / 34.872
        zscore = 0.77696 + 1.2566 * re8

        st.write("re1:", re1)
        st.write("re2:", re2)
        st.write("re3:", re3)
        st.write("re4:", re4)
        st.write("re5:", re5)
        st.write("re6:", re6)
        st.write("re7:", re7)
        st.write("re8:", re8)
        st.write("zscore:", zscore)

        if zscore < 0:
            result = (1 + np.exp(-zscore)) / 1  
        else:
            result = (1 + np.exp(zscore)) / 1 

        st.write("Resultado da fórmula (1 + e^-zscore) / 1:", result)

        st.success('Resultado da previsão: {}'.format(
            "Você teve um Bom Dia! (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)" 
            if result >= 50.0
            else "Você não teve um bom dia. (ISSO É UM TESTE, PODE DAR RESULTADOS NÃO PRECISOS)"
        ))
        print(result)

if __name__ == '__main__':
    main()


