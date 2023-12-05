import streamlit as st
# from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎲"
)

# image_path=PassaOcaminhoAqui

# =================
# Barra Lateral (Sidebar) do Streamlit
# =================
st.sidebar.markdown('# Curry Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")

st.write( "# Curry Company Growth Dashboard" )

st.markdown(
    """
    Growth Dashborad foi construido para acompanhar as métricas de crescimetno dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashborad?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregadores:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes.
    ### Ask for Help
    - Time de Data Science no Discord
       - @maxwelloliveira
""")
