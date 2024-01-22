import streamlit as st
from streamlit_image_comparison import image_comparison
import pandas as pd
import plotly.express as px
import time
from datetime import datetime
import locale

st.set_page_config(page_title="BBTS", page_icon=":shark",layout="wide")



# # Adicione um plano de fundo personalizado usando CSS
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #0074cc;  /* Substitua pela cor desejada em formato hexadecimal */
#             color: white;  /* Cor do texto no corpo */
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# today = datetime.datetime.now()
# next_year = today.year + 1
# jan_1 = datetime.date(next_year, 1, 1)
# dec_31 = datetime.date(next_year, 12, 31)


with st.container():
    st.header(':blue[BBTS]: Categorização de URLs BB')
    # st.subheader('Teste :blue[cool] :sunglasses:')
    #st.subheader("Categorização de URL's BB")
    st.divider()
#st.snow()

#with st.container():
# Using object notation
    
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")




@st.cache_data
def carregar_dados():
    tabela =  pd.read_csv("Report-17-01-2024_15-00-17.csv", sep=',')
    return tabela

df = carregar_dados()


#df
df["Data da solicitação"] = pd.to_datetime(df["Data da solicitação"], format="%d/%m/%Y")
df = df.sort_values("Data da solicitação")

# Extrair valores únicos de ano e mês (por extenso)
anos_unicos = df['Data da solicitação'].dt.year.unique().tolist()
meses_unicos = df['Data da solicitação'].dt.month_name(locale='pt_BR').str.capitalize().unique().tolist()


df["Mes/Ano"] = df["Data da solicitação"].apply(lambda x: str(x.month) +"-"+ str(x.year))
#print(df_mes)





# Criar a lista de opções para o seletor de mês
opcoes_mes_ano = ['Todos'] + df["Mes/Ano"].unique().tolist()
opcoes_ano = ['Todos'] + [str(ano) for ano in anos_unicos]
opcoes_status = ['Todos'] + df["Status"].unique().tolist()

# Sidebar para seleção do mês
with st.sidebar:
    # Selecionar ano e mês no Streamlit
    st.image("BancodoBrasil.Logomarca.VersãoPrincipal.Amarelo.RGB.png", use_column_width=True,  output_format="PNG")
    # st.image(r"C:\Users\geovanne.sales\Downloads\Logomarca_Comercial\Azul - Principal\RGB\BancodoBrasil.Logomarca.VersãoPrincipal.Azul.RGB.png", use_column_width=True)

    #month = st.sidebar.selectbox(":black[Mês]", opcoes_mes_ano)
    status = st.sidebar.selectbox("Escolha o Status", opcoes_status)


    # Remover 'Todos' da lista antes de converter para inteiro
    ano_escolhido_str = st.selectbox("Escolha o ano", opcoes_ano)
    if ano_escolhido_str != 'Todos':
        ano_escolhido = int(ano_escolhido_str)
    else:
        ano_escolhido = None

    # Definir as datas de início e fim do ano escolhido
    if ano_escolhido is not None:
        jan_1 = datetime(ano_escolhido, 1, 1)
        dec_31 = datetime(ano_escolhido, 12, 31)
        
        # Converter as datas para datetime64[ns]
        data_inicio = pd.to_datetime(st.date_input("Escolha a data de início", min_value=jan_1, max_value=dec_31, value=jan_1, format="DD.MM.YYYY"))
        data_fim = pd.to_datetime(st.date_input("Escolha a data de término", min_value=jan_1, max_value=dec_31, value=dec_31, format="DD.MM.YYYY"))
    
    

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# [theme]
# backgroundColor="#1631bb"
# secondaryBackgroundColor="#f3ff80"
# textColor="#f7f7f7"

# Filtrar os dados pelo Status selecionado
if status == 'Todos':
    df_filtrado = df  # Se "Todos" for selecionado, não aplicar filtro
    # df_filtrado
else:
    df_filtrado = df[df["Status"] == status]
    # df_filtrado

# Filtrar o DataFrame com base no intervalo de datas
if ano_escolhido_str == 'Todos':
    df_filtrado = df
    #df_filtrado
else:
    df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
    #df_filtrado

# d = st.date_input(
#         "Select your vacation for next year",
#         (jan_1, datetime.date(next_year, 1, 7)),
#         jan_1,
#         dec_31,
#         format="MM.DD.YYYY",
#     )
# d

operadores_url= df_filtrado.groupby("Operador Responsável")['URL'].count()
fig_operador = px.bar(operadores_url, x="URL",
                      title="Total Url por Operador")

# Adicionar cor de fundo ao layout
fig_operador.update_layout(
    paper_bgcolor='#1C1C1C',  # Cor de fundo #3269D6
    plot_bgcolor='#1C1C1C'  # Cor de fundo da área do gráfico
)
# Adicionar cor preta aos eixos
fig_operador.update_xaxes(
    linecolor='white',     # Cor da linha do eixo x
    gridcolor='white',     # Cor das linhas da grade do eixo x
    tickfont=dict(color='white'),  # Cor dos rótulos do eixo x
    titlefont=dict(color='white')  # Cor do título do eixo x
)
fig_operador.update_yaxes(
    linecolor='white',     # Cor da linha do eixo x
    #gridcolor='white',     # Cor das linhas da grade do eixo x
    tickfont=dict(color='white'),  # Cor dos rótulos do eixo y
    titlefont=dict(color='white')  # Cor do título do eixo y
)

with col1:
    st.plotly_chart(fig_operador)
# col1.plotly_chart(fig_operador)







# with col2:
    
# with col3:
# st.bar_chart(operadores_url, color="#ffaa0088")
# Filtrar os dados pelo mês selecionado
# Filtrar os dados pelo mês selecionado
# if month == 'Todos':
#     df_filtrado = df  # Se "Todos" for selecionado, não aplicar filtro
#     df_filtrado
# else:
#     df_filtrado = df[df["Mes/Ano"] == month]
#     df_filtrado

# # Filtrar o DataFrame com base no intervalo de datas
# if ano_escolhido_str == 'Todos' or status == "Todos":
#     df_filtrado = df
#     df_filtrado
# else:
#     df_filtrado = df[df["Status"] == status]
#     df_filtrado
#     df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
#     df_filtrado


# if status == 'Solicitado' or status == 'Em andamento' or status == 'Concluido' or status == 'Improcedente': 
#     df_filtrado = df[df["Status"] == status]
#     df_filtrado
# else:
#     df_filtrado = df
#     df_filtrado
# elif df_filtrado = df[(df["Data da solicitação"] >= data_inicio) & (df["Data da solicitação"] <= data_fim)]
#     df_filtrado

# Filtrar os dados pelo mês selecionado e pelo Status
if status == 'Todos' and ano_escolhido_str == 'Todos':
    df_filtrado = df  # Se todos forem selecionados como "Todos", não aplicar filtro
    df_filtrado
else:
    # # Aplicar filtros conforme necessário
    # df_filtrado = df.copy()  # Crie uma cópia do DataFrame original

    if status != 'Todos':
        df_filtrado = df_filtrado[df_filtrado["Status"] == status]
        

    if ano_escolhido_str != 'Todos':
        df_filtrado = df_filtrado[(df_filtrado["Data da solicitação"] >= data_inicio) & (df_filtrado["Data da solicitação"] <= data_fim)]
    df_filtrado