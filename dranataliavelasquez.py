import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Dra. Natalia Velásquez | Asesoría Farmacéutica",
    page_icon="🧪",
    layout="wide"
)

# Estilos personalizados para reflejar profesionalismo y estética
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #004d40;
        background-color: #004d40;
        color: white;
    }
    .highlight {
        color: #004d40;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Contacto Directo) ---
st.sidebar.image("https://via.placeholder.com/150", caption="QF. Natalia Velásquez") # Puedes reemplazar con su foto real
st.sidebar.title("Contacto")
st.sidebar.write("📧 nvelasquezqf@gmail.com")
st.sidebar.write("📞 +57 315 270 5617")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/natalia-velásquez-g/)")

# --- HEADER ---
st.title("🧪 QF. Natalia Velásquez M.Sc")
st.subheader("Asesoría Farmacéutica, Cosmética y Formulación")
st.write("Experta en Gestión de Calidad e impulsando el éxito de empresas comprometidas.")

st.divider()

# --- SECCIÓN: PERFIL PROFESIONAL ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Sobre Natalia")
    st.write("""
    Química Farmacéutica, Especialista Universitaria en Docencia y Magíster en Formulación de Productos Químicos. 
    Con una trayectoria impecable como auditora certificada y docente, mi enfoque es proactivo y orientado 
    a resultados que empoderan a empresas y emprendedores a alcanzar sus objetivos de cumplimiento normativo.
    """)
    st.info("**Enfoque:** Calidad desde el diseño (QbD) y mejora continua.")

with col2:
    st.header("Colaboraciones")
    st.write("- Colegio Nacional de Químicos Farmacéuticos")
    st.write("- Coopidrogas")
    st.write("- Universidad ICESI (GRUPROC)")
    st.write("- Meditec / Droccidente")

# --- SECCIÓN: SERVICIOS (Portafolio) ---
st.divider()
st.header("Portafolio de Servicios")

servicios = {
    "Gestión de Calidad": [
        "Estudios de Estabilidad (Vida útil real)",
        "Gestión Documental (SOPs a medida)",
        "Buenas Prácticas de Manufactura (BPM)"
    ],
    "Desarrollo e Innovación": [
        "Formulación exclusiva de Cosméticos",
        "Formulación de Suplementos Dietarios",
        "Enfoque Quality by Design (QbD)"
    ],
    "Auditoría y Entrenamiento": [
        "Autoinspecciones y Auditorías Internas",
        "Programas de entrenamiento técnico-normativo",
        "Soporte para Notificación Sanitaria (NSO)"
    ]
}

cols = st.columns(3)
for i, (categoria, items) in enumerate(servicios.items()):
    with cols[i]:
        st.subheader(categoria)
        for item in items:
            st.write(f"✅ {item}")

# --- SECCIÓN: DETALLE TÉCNICO ---
with st.expander("Ver detalle de normativas manejadas"):
    st.write("""
    - **Cosméticos:** Resolución 2206 de 2021.
    - **Suplementos Dietarios:** Resolución 2015 de 2011.
    """)

# --- FOOTER ---
st.divider()
st.caption("Página diseñada para la Dra. Natalia Velásquez - 2026. Todos los derechos reservados.")