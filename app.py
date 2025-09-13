import streamlit as st

st.set_page_config(page_title="Calculadora MRUA", page_icon="🧪")
st.title("🧪 Calculadora de Movimiento Rectilíneo Uniformemente Acelerado (MRUA)")

st.write("""
Esta herramienta te permite calcular diferentes variables del Movimiento Rectilíneo Uniformemente Acelerado (MRUA):

- Posición final
- Velocidad final
- Tiempo
- Aceleración
""")

opcion = st.selectbox("¿Qué variable deseas calcular?", ["Posición Final (x)", "Velocidad Final (v)"])

if opcion == "Posición Final (x)":
    st.subheader("Fórmula: x = x₀ + v₀·t + ½·a·t²")
    x0 = st.number_input("Posición inicial (x₀) en metros", value=0.0)
    v0 = st.number_input("Velocidad inicial (v₀) en m/s", value=0.0)
    t = st.number_input("Tiempo (t) en segundos", min_value=0.0, value=0.0)
    a = st.number_input("Aceleración (a) en m/s²", value=0.0)

    if st.button("Calcular posición final"):
        x = x0 + v0 * t + 0.5 * a * t ** 2
        st.success(f"📍 Posición final: {round(x, 4)} m")
        if a == 0:
            st.info("ℹ️ No hay aceleración: el movimiento es uniforme.")

elif opcion == "Velocidad Final (v)":
    st.subheader("Fórmula: v = v₀ + a·t")
    v0 = st.number_input("Velocidad inicial (v₀) en m/s", value=0.0)
    a = st.number_input("Aceleración (a) en m/s²", value=0.0)
    t = st.number_input("Tiempo (t) en segundos", min_value=0.0, value=0.0)

    if st.button("Calcular velocidad final"):
        v = v0 + a * t
        st.success(f"💨 Velocidad final: {round(v, 4)} m/s")
        if a == 0:
            st.info("ℹ️ La aceleración es cero: velocidad constante.")

st.markdown("---")
st.caption("Desarrollado con ❤️ usando Streamlit")
