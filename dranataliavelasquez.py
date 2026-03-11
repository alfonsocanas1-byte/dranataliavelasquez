import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Dra. Natalia Velásquez | Asesoría Farmacéutica",
    page_icon="🌿",
    layout="wide"
)

# Estilos personalizados en VERDE para sorprenderla
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background-color: #f0f7f4;
    }
    /* Encabezados en verde esmeralda */
    h1, h2, h3 {
        color: #1b5e20 !important;
    }
    /* Botones y acentos */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: #e8f5e9;
    }
    /* Tarjetas informativas */
    .stAlert {
        background-color: #e8f5e9;
        border: 1px solid #c8e6c9;
    }
    /* Estilo para el sidebar */
    [data-testid="stSidebar"] {
        background-color: #1b5e20;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## Contacto Directo")
    st.write("📧 nvelasquezqf@gmail.com")
    st.write("📞 +57 315 270 5617")
    st.markdown("---")
    st.write("🔗 [LinkedIn Profesional](https://www.linkedin.com/in/natalia-velásquez-g/)")
    st.info("Ubicación: Colombia 🇨🇴")

# --- CONTENIDO PRINCIPAL ---
col_logo, col_title = st.columns([1, 4])

with col_title:
    st.title("QF. Natalia Velásquez M.Sc")
    st.markdown("### **Magíster en Formulación de Productos Químicos**")
    st.write("Impulsando el éxito de empresas comprometidas con la calidad y la salud.")

st.divider()

# --- SECCIÓN: EXPERIENCIA Y PERFIL ---
st.header("🌿 Perfil Profesional")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    Como experta en **Gestión de Calidad, Farmacéutica y Cosmética**, mi enfoque se centra en la 
    excelencia técnica y el cumplimiento normativo riguroso. Con amplia experiencia en 
    consultoría de sistemas de calidad y auditoría certificada, transformo procesos complejos 
    en resultados tangibles. [cite: 5, 6, 7, 23, 24]
    """)
    
    st.success("**Especialidades:** Formulación de Suplementos Dietarios y Cosméticos bajo estándares internacionales. [cite: 9, 10, 11]")

with col2:
    st.markdown("#### **Colaboraciones Destacadas**")
    st.write("🧪 Colegio Nacional de QF [cite: 40]")
    st.write("🧪 Universidad ICESI [cite: 43]")
    st.write("🧪 Coopidrogas [cite: 41]")
    st.write("🧪 Droccidente [cite: 49]")

st.divider()

# --- SECCIÓN: SERVICIOS ---
st.header("📋 Portafolio de Servicios Especializados")

# Organizado por categorías técnicas
tabs = st.tabs(["Estabilidad y Calidad", "Desarrollo y Formulación", "Auditoría y Normas"])

with tabs[0]:
    st.subheader("Control y Aseguramiento")
    st.write("- **Estudios de Estabilidad:** Diseño de protocolos para determinar vida útil real. [cite: 60, 65]")
    st.write("- **Gestión Documental:** Construcción de SOPs bajo Resoluciones 2206 (Cosméticos) y 2015 (Suplementos). [cite: 70, 73]")
    st.write("- **BPM:** Implementación de Buenas Prácticas de Manufactura. [cite: 82]")

with tabs[1]:
    st.subheader("Innovación de Productos")
    st.write("- **Formulación Exclusiva:** Diseño de prototipos cosméticos y dietarios. [cite: 117, 121]")
    st.write("- **Quality by Design (QbD):** Calidad desde la concepción del diseño. [cite: 123]")
    st.write("- **Escalamiento:** Asesoría técnica en el proceso de producción industrial. [cite: 125]")

with tabs[2]:
    st.subheader("Cumplimiento y Capacitación")
    st.write("- **Auditorías Internas:** Autoinspecciones sistemáticas para reducción de riesgos. [cite: 127, 131]")
    st.write("- **Entrenamientos:** Programas técnico-normativos a medida para el personal. [cite: 92, 95]")
    st.write("- **Soporte Legal:** Apoyo en solicitudes de Notificación Sanitaria Obligatoria. [cite: 126]")

# --- CIERRE ---
st.divider()
st.center = st.markdown(
    "<div style='text-align: center; color: #1b5e20;'><b>Calidad, Rigor y Ética Profesional</b></div>", 
    unsafe_allow_html=True
)