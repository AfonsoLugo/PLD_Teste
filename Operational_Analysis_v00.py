import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

"""
# Análise de Geração x PLD sombra
Esta é a tabela gerada pelos algoritmos do ePowerBay:
"""
df = pd.read_csv('Projetos_Hora_201908-202008_v00.csv')

df_fcpld = df.set_index(['Usina', 'Submercado', 'Fonte']).groupby(level=['Usina', 'Submercado', 'Fonte']).mean().sort_values('FC PLD Sombra', ascending = False).reset_index()

df_fcpld[['Usina', 'Submercado', 'Fonte', 'Potência_(MW)', 'FC PLD Sombra']]

map_data = df_fcpld[['lat', 'lon']][0:20]

st.map(map_data)

df_trans = df_fcpld.iloc[0:20].sort_values('FC PLD Sombra', ascending = False).T


new_header = df_trans.iloc[0]
df_trans = df_trans[1:]
df_trans.columns = new_header
#df_trans

"""
O gráfico abaixo mostra os 20 projetos eólicos com o maior FC x PLD Sombra médio nos últimos 12 meses
"""
st.line_chart(df_trans.iloc[10])

df_ger = df.set_index(['Usina', 'Submercado', 'Fonte']).groupby(level=['Usina', 'Submercado', 'Fonte']).sum().sort_values('Geracao_(MWh)', ascending = False).reset_index()

df_ger[['Usina', 'Submercado', 'Geracao_(MWh)']][0:20]

df_trans2 = df_ger.iloc[0:20].sort_values('Geracao_(MWh)', ascending = False).T
new_header2 = df_trans2.iloc[0]
df_trans2 = df_trans2[1:]
df_trans2.columns = new_header2
#df_trans2

"""
O gráfico abaixo mostra os 20 projetos eólicos com o maior geração nos últimos 12 meses
"""
st.line_chart(df_trans2.iloc[6])
st.line_chart(df_ger['Geracao_(MWh)'][0:20])

################################################################








#################################################################

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['EOL', 'UFV'])

    st.line_chart(chart_data)

option = st.selectbox(
'Qual usina você quer analisar?',
    df_fcpld['Usina'])

'You selected: ', option

fig = plt.figure(figsize = (12,6))
ax1 = fig.add_subplot(111)

mes = ['Ago/19', 'Set/19', 'Out/19', 'Nov/19', 'Dez/19', 'Jan/20', 'Fev/20', 'Mar/20', 'Abr/20', 'Mai/20', 'Jun/20', 'Jul/20']
horario = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

df_pld_ne = pd.read_csv('PLD_Mensal_Nordeste_2019-202007_v00.csv')
df_eol_mes = df_eol.set_index(['Usina', 'Ano', 'Mês']).groupby(level = ['Usina', 'Ano', 'Mês']).mean().reset_index()
zero = 12*[0]


ax1.bar(mes, df_pld_ne['PLD_Sombra'][7:], label = 'PLD Sombra', color = '#B4B2B0', zorder=2)
ax1.grid(True)
ax1.set_ylim(0,500)
ax1.tick_params(labelsize = 14)
ax1.set_ylabel('PLD [R$/MWh]', size = 14)
ax1.legend(bbox_to_anchor=(0.25, -0.05), loc='upper center', fontsize = 12)
ax2 = ax1.twinx()

nome = option
lista = df_eol_mes.index[df_eol_mes["Usina"] == nome].tolist()
y = df_eol_mes['FC'][lista[0:12]]
ax2.plot(mes, y, linewidth=2, label = nome, zorder=3)

ax2.axhline(0, linestyle='--', color = 'black', zorder =3)
ax2.grid(False)
ax2.set_ylim(0,1)
ax2.set_ylabel('FC', size = 14)
ax2.tick_params(labelsize = 13)
ax2.legend(bbox_to_anchor=(0.6, -0.05), loc='upper center', ncol = 3, fontsize = 12)
plt.tight_layout()

st.pyplot(fig)

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Clique Aqui!')
if pressed:
    right_column.write("Você acabou de gerar 01 ePowerCoin para a equipe ePowerBay. Obrigado!")

expander = st.beta_expander("Conceitos")
expander.write("PLD é o Preço Líquido das Diferenças.")
expander.write('O PLD é apurado com base no CMO que é obtido por meio dos meio dos modelos computacionais utilizados pelo ONS para realizar o planejamento de operação do sistema. ')
expander.write('CMO é o Custo Marginal de Operação, ou seja, o custo para de produzir o próximo MWh.')
