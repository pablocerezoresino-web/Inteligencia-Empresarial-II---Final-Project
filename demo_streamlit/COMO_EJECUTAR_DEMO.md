# Cómo ejecutar la demo interactiva — 50 Doctors Sistema Agéntico

## Requisitos previos
- Python 3.9 o superior instalado (`py --version` en Windows / `python3 --version` en Mac/Linux)
- Git instalado y el repositorio clonado en tu máquina

## Pasos para ejecutar

### 1. Clona el repositorio (si no lo tienes)
```bash
git clone https://github.com/adrianjulve-lang/Inteligencia-Empresarial-II---Final-Project.git
cd Inteligencia-Empresarial-II---Final-Project
```

### 2. Instala las dependencias
```bash
# Windows
py -m pip install -r demo_streamlit/requirements.txt

# Mac / Linux
pip3 install -r demo_streamlit/requirements.txt
```

### 3. Lanza la demo
```bash
# Windows
py -m streamlit run demo_streamlit/app.py

# Mac / Linux
python3 -m streamlit run demo_streamlit/app.py
```

### 4. Abre el navegador
Streamlit abrirá automáticamente `http://localhost:8501` en tu navegador.
Si no abre, cópialo manualmente.

---

## Módulos disponibles en la demo

| Módulo | Descripción |
|--------|-------------|
| 🎯 Dashboard Ejecutivo | Métricas globales, árbol de decisión, escenarios, trazabilidad |
| 🔍 Análisis AMC | Ejecuta los 4 agentes en tiempo real y muestra scores Sanitas/Adeslas/Asisa |
| 🚨 Early Warning System | Dashboard 9 KIIs con simulación de alertas interactiva |
| 💬 Pregunta al Agente | Preguntas en lenguaje natural sobre el proyecto |

---

## Guión sugerido para la presentación al profesor

1. **Abre el Dashboard Ejecutivo** → muestra el veredicto CONDITIONAL GO y el árbol de decisión
2. **Ve a Análisis AMC** → haz clic en "Ejecutar Agente AMC" y muestra los 4 agentes corriendo
3. **Ve a Early Warning** → haz clic en "KIT2 en ROJO" para simular una alerta regulatoria
4. **Ve a Pregunta al Agente** → escribe "¿Cómo reaccionará Sanitas?" y muestra la respuesta

Tiempo estimado de demo: **5-8 minutos**

---

## Problemas frecuentes

**Error: "streamlit not found"**
```bash
py -m pip install streamlit
```

**Error: "ModuleNotFoundError"**
Asegúrate de lanzar la demo desde la raíz del repositorio, no desde dentro de `demo_streamlit/`.

**Puerto 8501 ocupado**
```bash
py -m streamlit run demo_streamlit/app.py --server.port 8502
```
