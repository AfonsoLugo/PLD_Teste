import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df_raw = pd.read_csv('Projetos_Hora_201908-202008_v00.csv')

df=df_raw


# General Statistics

st.title('Análise da Geração e do PLD')

"""
Este aplicativo tem como objetivo analisar a geração de pasques eólicos e solares.
"""

# Analysis per Usina #

# Selecionar a fonte que será analisada #
option1 = st.selectbox(
'Selecione o tipo de usina',
['EOL', 'UFV'])

# Data frame com a fonte selecionada anteriormente #
df_f = df.loc[df.Fonte == option1]

# Selecionar qual usina será analisada #
option2 = st.selectbox(
'Selecione o nome da usina',
df_f.groupby('Usina').sum().reset_index()['Usina'])
'Você selecionou a usina ', option2

df_n = df_f.loc[df_f['Usina'] == option2]

option3 = st.selectbox(
'O que você quer analisar?',
    [df_n.columns[12], df_n.columns[13], df_n.columns[14], df_n.columns[16]])

option4 = st.selectbox(
'Selecione o ano',
    df_n.groupby('Ano').sum().reset_index()['Ano'])

df_ano = df_n.set_index(['Ano', 'Mês']).groupby(level=['Ano', 'Mês']).sum().reset_index()

option5 = st.selectbox(
'Selecione o mês',
    df_ano.groupby('Mês').sum().reset_index()['Mês'])

df_h = df_n.loc[df_n['Ano'] == option4].loc[df_n['Mês'] == option5]

### PLOT DO GRÁFICO ###
fig1 = plt.figure(figsize = (12,6))
ax1 = fig1.add_subplot(111)

horario = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

ax1.bar(horario, df_h['PLD Sombra'], label = 'PLD Sombra', color = '#B4B2B0', zorder=2)
ax1.grid(True)
#ax1.set_ylim(0,500)
ax1.tick_params(labelsize = 14)
ax1.set_ylabel('PLD [R$/MWh]', size = 14)
ax1.legend(bbox_to_anchor=(0.25, -0.05), loc='upper center', fontsize = 12)

ax2 = ax1.twinx()

ax2.plot(horario, df_h[option3], linewidth=2, label = option2, zorder=3)
ax2.grid(False)
ax2.set_ylabel(option3, size = 14)
ax2.tick_params(labelsize = 13)
ax2.legend(bbox_to_anchor=(0.6, -0.05), loc='upper center', ncol = 3, fontsize = 12)
plt.tight_layout()

st.pyplot(fig1)
