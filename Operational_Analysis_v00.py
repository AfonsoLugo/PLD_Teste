import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

st.title('Customer Service')
"""
This report is an analysis of the tickets answered by Afonso Lugo for the Tier 1 English and Portuguese tickets in LocalBitcoins.
"""
"""
The main objective of this report is to provide insights of the problems faced by the users of LocalBitcoins platform.
"""
"""
Data is collected manually and classified according to the categories in “Support types and tiers” and adapted with the experience. In this report, data is presented from November 2nd on, and only the tickets which got answered to the user are counted (close and assignments are not included). This application is planned to update once per week.
"""

df_raw = pd.read_csv('Projetos_Hora_201908-202008_v00.csv')

df=df_raw

#week_s1 = week_sum.T.reset_index()
#week_s1 = week_s1.drop(week_s1.index[0])
#week_s1 = week_s1.rename(columns={week_s1.columns[0]: "Type", week_s1.columns[1]: "Week 43"})


# General Statistics

st.title('Análise da Geração e do PLD')

"""
From week 45 to week 48 of 2020, more than 1800 tickets were answered with an average of 455 per week and 91 tickets per day.
"""

# Analysis per Week #

"""
**Now you can analyse in details each week.**
"""

# Selecionar a fonte que será analisada #
option1 = st.selectbox(
'Selecione o tipo de usina',
['EOL', 'UFV'])

# Data frame com a fonte selecionada anteriormente #
df_f = df.loc[df.Fonte == option1]

# Selecionar qual usina será analisada #
option2 = st.selectbox(
'Selecione o nome da usina',
df_f['Usina'])
'Você selecionou a usina ', option2

df_n = df_f.loc[df_f['Usina'] == option2]

option3 = st.selectbox(
'O que você quer analisar?',
    [df_n.columns[12], df_n.columns[13], df_n.columns[14], df_n.columns[16]])


### PLOT DO GRÁFICO ###
fig1 = plt.figure(figsize = (12,6))
ax1 = fig.add_subplot(111)

horario = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

ax1.bar(horario, df_n['PLD Sombra'], label = 'PLD Sombra', color = '#B4B2B0', zorder=2)
ax1.grid(True)
ax1.set_ylim(0,500)
ax1.tick_params(labelsize = 14)
ax1.set_ylabel('PLD [R$/MWh]', size = 14)
ax1.legend(bbox_to_anchor=(0.25, -0.05), loc='upper center', fontsize = 12)

ax2 = ax1.twinx()

ax2.plot(horario, df_n[option3], linewidth=2, label = nome, zorder=3)
ax2.axhline(0, linestyle='--', color = 'black', zorder =3)
ax2.grid(False)
ax2.set_ylim(0,1)
ax2.set_ylabel('FC', size = 14)
ax2.tick_params(labelsize = 13)
ax2.legend(bbox_to_anchor=(0.6, -0.05), loc='upper center', ncol = 3, fontsize = 12)
plt.tight_layout()

st.pyplot(fig1)
