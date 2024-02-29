import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import locale

# [theme]
# base="dark"
# secondaryBackgroundColor="#222d94"


st.set_page_config(page_title="BBTS", page_icon="BancodoBrasil.Logomarca.VersãoPrincipal.Amarelo.RGB.png",layout="wide")

col1,col2 = st.columns(2) 
with col1:
    st.image("BancodoBrasil.Logomarca.VersãoPrincipal.Amarelo.RGB.png", use_column_width=False,  output_format="PNG")

with col2:
    st.markdown("<p style='color: yellow; font-size: 60px;'>Gerando valor e <br> eficiência para nossos <br> clientes por meio de soluções inteligentes.</p>", unsafe_allow_html=True)

st.divider()

st.title(':blue[Navegue] pelos nossos DASHBOARDS!')
# st.subheader('Teste :blue[cool] :sunglasses:')
#st.subheader("Categorização de URL's BB")
st.divider()

# homepage = st.button("Home")
page_1 = st.button("BBTS Categorização URL(s)")
page_2 = st.button("DDOS")
page_3= st.link_button("BBAmericas_Painel", "https://app.powerbi.com/links/7mhiLo4N5V?ctid=ffc0be44-315f-4479-b12f-56afe6ededd6&pbi_source=linkShare")
page_4= st.link_button("BBTS_Painel", "https://app.powerbi.com/links/WooPu4Kw3v?ctid=ffc0be44-315f-4479-b12f-56afe6ededd6&pbi_source=linkShare")

# #with st.container():
# if homepage:
#     st.switch_page("homepage.py")

#st.page_link("your_app.py", label="Home", icon="🏠")
# st.page_link("pages/Categorização_Url.py", label="BBTS Categorização URL(s)")
# st.page_link("pages/DDOS.py", label="DDOS")
# st.page_link("https://app.powerbi.com/links/7mhiLo4N5V?ctid=ffc0be44-315f-4479-b12f-56afe6ededd6&pbi_source=linkShare", label="BBAmericas_Painel")
# st.page_link("https://app.powerbi.com/links/WooPu4Kw3v?ctid=ffc0be44-315f-4479-b12f-56afe6ededd6&pbi_source=linkShare", label="BBTS_Painel")


if page_1:
    st.switch_page("pages/Categorização_Url.py")
if page_2:
    st.switch_page("pages/DDOS.py")


    
# st.header(':blue[BBTS]: Categorização de URLs BB')
# # st.subheader('Teste :blue[cool] :sunglasses:')
# #st.subheader("Categorização de URL's BB")
# st.divider()





# @st.cache_data
# def carregar_dados():
#     tabela =  pd.read_csv("Report-25-01-2024_15-32-34.csv", sep=',')
#     return tabela

# df = carregar_dados()

# # try:
# #     locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
# # except locale.Error:
# #     print("Locale 'pt_BR' not available, using default locale.")

# #df
# df["Data da solicitação"] = pd.to_datetime(df["Data da solicitação"], format="%d/%m/%Y")
# df = df.sort_values("Data da solicitação")

# # Extrair valores únicos de ano e mês (por extenso)
# anos_unicos = df['Data da solicitação'].dt.year.unique().tolist()
# #meses_unicos = df['Data da solicitação'].dt.month_name(locale='pt_BR').str.capitalize().unique().tolist()


# df["Mes/Ano"] = df["Data da solicitação"].apply(lambda x: str(x.month) +"-"+ str(x.year))
# #print(df_mes)





# # Criar a lista de opções para o seletor de mês
# opcoes_mes_ano = ['Todos'] + df["Mes/Ano"].unique().tolist()
# opcoes_ano = ['Todos'] + [str(ano) for ano in anos_unicos]
# opcoes_status = ['Todos'] + df["Status"].unique().tolist()
# #opcoes_meses = ['Todos'] + meses_unicos
# opcoes_operadores = ['Todos'] + df["Operador Responsável"].unique().tolist()

# # Sidebar para seleção do mês
# with st.sidebar:
#     # Selecionar ano e mês no Streamlit
#     st.image("BancodoBrasil.Logomarca.VersãoPrincipal.Amarelo.RGB.png", use_column_width=True,  output_format="PNG")
#     # st.image(r"C:\Users\geovanne.sales\Downloads\Logomarca_Comercial\Azul - Principal\RGB\BancodoBrasil.Logomarca.VersãoPrincipal.Azul.RGB.png", use_column_width=True)

#     #month = st.sidebar.selectbox(":black[Mês]", opcoes_mes_ano)
#     status = st.selectbox("Escolha o Status", opcoes_status)


#     # Remover 'Todos' da lista antes de converter para inteiro
#     ano_escolhido_str = st.selectbox("Escolha o ano", opcoes_ano)
#     if ano_escolhido_str != 'Todos':
#         ano_escolhido = int(ano_escolhido_str)
#     else:
#         ano_escolhido = None

#     # Definir as datas de início e fim do ano escolhido
#     if ano_escolhido is not None:
#         jan_1 = datetime(ano_escolhido, 1, 1)
#         dec_31 = datetime(ano_escolhido, 12, 31)
        
#         # Converter as datas para datetime64[ns]
#         data_inicio = pd.to_datetime(st.date_input("Escolha a data de início", min_value=jan_1, max_value=dec_31, value=jan_1, format="DD.MM.YYYY"))
#         data_fim = pd.to_datetime(st.date_input("Escolha a data de término", min_value=jan_1, max_value=dec_31, value=dec_31, format="DD.MM.YYYY"))
    
    
#     operadores_sidebar = st.selectbox("Escolha o Operador Responsável", opcoes_operadores)
#     #meses_sidebar = st.multiselect('Escolha o Mês', opcoes_meses, defaut='Todos')
    

# col1, col2 = st.columns(2)
# # col3, col4, col5 = st.columns(3)

# # [theme]
# # backgroundColor="#1631bb"
# # secondaryBackgroundColor="#272726"
# # textColor="#f7f7f7"

# # # Filtrar os dados pelo Status selecionado
# # if status == 'Todos':
# #     df_filtrado = df  # Se "Todos" for selecionado, não aplicar filtro
# #     # df_filtrado
# # else:
# #     df_filtrado = df[df["Status"] == status]
# #     # df_filtrado

# # # Filtrar o DataFrame com base no intervalo de datas
# # if ano_escolhido_str == 'Todos':
# #     df_filtrado = df
# #     #df_filtrado
# # else:
# #     df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
# #     #df_filtrado


# # Filtrar os dados pelo mês selecionado e pelo Status
# #if status == 'Todos' and ano_escolhido_str == 'Todos' and meses_sidebar == 'Todos':
# if status == 'Todos' and ano_escolhido_str == 'Todos' and operadores_sidebar == 'Todos':
#         df_filtrado = df  # Se todos forem selecionados como "Todos", não aplicar filtro
#     # df_filtrado
# else:
#     # # Aplicar filtros conforme necessário
#     # df_filtrado = df.copy()  # Crie uma cópia do DataFrame original

#     if status != 'Todos':
#         df_filtrado = df[df["Status"] == status]
        

#     if ano_escolhido_str != 'Todos':
#         df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
#     # df_filtrado
#     # if meses_sidebar != 'Todos':
#     #     meses_filtrados = df["Data da solicitação"].dt.month_name(locale='pt_BR').str.capitalize()
#     #     df_filtrado = df[meses_filtrados.isin(meses_sidebar)]
#     if operadores_sidebar != 'Todos':
#         df_filtrado = df[df["Operador Responsável"] == operadores_sidebar]




# operadores_url= df_filtrado.groupby("Operador Responsável")['URL'].count()
# fig_operador = px.bar(operadores_url, x="URL",
#                       title="Total Url por Operador")

# # Adicionar cor de fundo ao layout
# fig_operador.update_layout(
#     paper_bgcolor='#1C1C1C',  # Cor de fundo #3269D6
#     plot_bgcolor='#1C1C1C'  # Cor de fundo da área do gráfico
# )
# # Adicionar cor preta aos eixos
# fig_operador.update_xaxes(
#     linecolor='white',     # Cor da linha do eixo x
#     gridcolor='white',     # Cor das linhas da grade do eixo x
#     tickfont=dict(color='white'),  # Cor dos rótulos do eixo x
#     titlefont=dict(color='white')  # Cor do título do eixo x
# )
# fig_operador.update_yaxes(
#     linecolor='white',     # Cor da linha do eixo x
#     #gridcolor='white',     # Cor das linhas da grade do eixo x
#     tickfont=dict(color='white'),  # Cor dos rótulos do eixo y
#     titlefont=dict(color='white')  # Cor do título do eixo y
# )

# with col1:
#     if operadores_sidebar == 'Todos':
#         st.subheader('Total de Url por Operador')
#     else:
#         st.subheader(f"Operador: :blue[{operadores_sidebar}] categorizou :red[{df_filtrado.loc[df_filtrado['Operador Responsável']==operadores_sidebar,'URL'].count()}] URL(s)")

#     st.plotly_chart(fig_operador)
# # col1.plotly_chart(fig_operador)




# soma_url = df_filtrado['URL'].count()
# volumeMensal_url = df_filtrado.groupby("Mes/Ano")["URL"].count()
# fig_volumeMensal_url = px.bar(volumeMensal_url, x="URL", title='Volume Mensal Url', color_discrete_sequence=['red'])

# # Adicionar cor de fundo ao layout
# fig_volumeMensal_url.update_layout(
#     paper_bgcolor='#1C1C1C',  # Cor de fundo #3269D6
#     plot_bgcolor='#1C1C1C'  # Cor de fundo da área do gráfico
# )
# # Adicionar cor preta aos eixos
# fig_volumeMensal_url.update_xaxes(
#     linecolor='white',     # Cor da linha do eixo x
#     gridcolor='white',     # Cor das linhas da grade do eixo x
#     tickfont=dict(color='white'),  # Cor dos rótulos do eixo x
#     titlefont=dict(color='white')  # Cor do título do eixo x
# )
# fig_volumeMensal_url.update_yaxes(
#     linecolor='white',     # Cor da linha do eixo x
#     #gridcolor='white',     # Cor das linhas da grade do eixo x
#     tickfont=dict(color='white'),  # Cor dos rótulos do eixo y
#     titlefont=dict(color='white')  # Cor do título do eixo y
# )

# with col2:
#     st.subheader(f'Total URL: :red[{soma_url}]')
#     #st.metric(label="Contador URL", value=soma_url)
#     st.plotly_chart(fig_volumeMensal_url)
    





# # with col3:
# # st.bar_chart(operadores_url, color="#ffaa0088")
# # Filtrar os dados pelo mês selecionado
# # Filtrar os dados pelo mês selecionado
# # if month == 'Todos':
# #     df_filtrado = df  # Se "Todos" for selecionado, não aplicar filtro
# #     df_filtrado
# # else:
# #     df_filtrado = df[df["Mes/Ano"] == month]
# #     df_filtrado

# # # Filtrar o DataFrame com base no intervalo de datas
# # if ano_escolhido_str == 'Todos' or status == "Todos":
# #     df_filtrado = df
# #     df_filtrado
# # else:
# #     df_filtrado = df[df["Status"] == status]
# #     df_filtrado
# #     df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
# #     df_filtrado


# # if status == 'Solicitado' or status == 'Em andamento' or status == 'Concluido' or status == 'Improcedente': 
# #     df_filtrado = df[df["Status"] == status]
# #     df_filtrado
# # else:
# #     df_filtrado = df
# #     df_filtrado
# # elif df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
# #     df_filtrado

# # Filtrar os dados pelo mês selecionado e pelo Status
# if status == 'Todos' and ano_escolhido_str == 'Todos' and operadores_sidebar == 'Todos':
#     df_filtrado = df  # Se todos forem selecionados como "Todos", não aplicar filtro
#     df_filtrado
# else:
#     # # Aplicar filtros conforme necessário
#     # df_filtrado = df.copy()  # Crie uma cópia do DataFrame original

#     if status != 'Todos':
#         df_filtrado = df_filtrado[df_filtrado["Status"] == status]

#     if ano_escolhido_str != 'Todos':
#         df_filtrado = df_filtrado[(df_filtrado["Data da solicitação"] >= data_inicio) & (df_filtrado["Data da solicitação"] <= data_fim)]
    

#     # if meses_sidebar != 'Todos':
#     #     meses_filtrados = df_filtrado["Data da solicitação"].dt.month_name(locale='pt_BR').str.capitalize()
#     #     df_filtrado = df_filtrado[meses_filtrados.isin(meses_sidebar)]
#     if operadores_sidebar != 'Todos':
#         df_filtrado = df_filtrado[df_filtrado["Operador Responsável"] == operadores_sidebar]
    
#     df_filtrado
        