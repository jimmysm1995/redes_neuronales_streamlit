import streamlit as st

st.title("Redes neuronales")
st.image("https://www.psycolab.com/wp-content/uploads/15286-scaled.jpg", width=600)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Una neurona con una entrada (y un peso)",
                            "Una neurona con dos entradas (y dos pesos)",
                            "Una neurona con tres entradas y bias (sesgo)"])

# Content for Tab 1
with tab1:
    st.header("Una neurona con una entrada (y un peso)")
    peso = 0.5
    st.write(f"El peso de las entradas es {peso}")
    entrada = st.slider("Seleccione el valor de la entrada:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_00")
    st.write(f"La salida de la neurona es {entrada * peso}")

# Content for Tab 2
with (tab2):
    st.header("Una neurona con dos entradas (y dos pesos)")
    peso0, peso1 = 1.5, 2.5
    st.write(f"Los pesos de las entradas son {peso0} y {peso1}")
    entrada0 = st.slider("Seleccione el valor de la entrada 0:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_10")
    entrada1 = st.slider("Seleccione el valor de la entrada 1:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_11")
    st.write(f"La salida de la neurona es {entrada0 * peso0 + entrada1 * peso1}")
# Content for Tab 3
with tab3:
    st.header("Una neurona con tres entradas y bias (sesgo)")
    peso0, peso1, peso2 = 1, 2, 3
    bias = 10
    st.write(f"Los pesos de las entradas son {peso0}, {peso1} y {peso2} y el bias es {bias}")
    entrada0 = st.slider("Seleccione el valor de la entrada 0:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_20")
    entrada1 = st.slider("Seleccione el valor de la entrada 1:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_21")
    entrada2 = st.slider("Seleccione el valor de la entrada 2:", min_value=0.0, max_value=100.0, step=0.1, key="entrada_22")
    st.write(f"La salida de la neurona es {entrada0 * peso0 + entrada1 * peso1 + entrada2 * peso2 + bias}")