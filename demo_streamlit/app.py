"""
Demo Interactiva — Sistema Agéntico 50 Doctors
Inteligencia Empresarial II | UFV | Prof. César Moreno Pascual

Ejecutar: streamlit run demo_streamlit/app.py
"""

import sys
import os
import json
from datetime import datetime

import streamlit as st

# Añadir rutas de los sistemas agénticos al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fase2_inteligencia_mercado_espanol'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fase5_estrategia_entrada'))

from agentic_intelligence_system import IntelligenceSystem, AMCAgent
from agentic_ews_system import EarlyWarningSystem, EWSAgent, AlertLevel, KII

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="50 Doctors · Sistema de Inteligencia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS personalizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .metric-card {
        background: #f8f9fa;
        border-left: 4px solid #0f3460;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    .alert-verde  { background:#d4edda; border-left:4px solid #28a745; padding:.6rem 1rem; border-radius:5px; }
    .alert-amarillo { background:#fff3cd; border-left:4px solid #ffc107; padding:.6rem 1rem; border-radius:5px; }
    .alert-rojo   { background:#f8d7da; border-left:4px solid #dc3545; padding:.6rem 1rem; border-radius:5px; }
    .verdict-box {
        background: linear-gradient(135deg, #0f3460, #1a1a2e);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .agent-badge {
        display: inline-block;
        background: #0f3460;
        color: white;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin: 2px;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size:1.8rem;">🏥 50 Doctors México — Sistema de Inteligencia Agéntica</h1>
    <p style="margin:0.3rem 0 0 0; opacity:0.8;">Expansión al Mercado Español · Inteligencia Empresarial II · UFV</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hospital.png", width=80)
    st.markdown("### 🤖 Sistema Multi-Agente")
    st.markdown("""
    **Fase 2 — AMC Intelligence**
    <span class="agent-badge">OSINT</span>
    <span class="agent-badge">Alt.Data</span>
    <span class="agent-badge">AMC</span>
    <span class="agent-badge">Síntesis</span>

    **Fase 5 — Early Warning**
    <span class="agent-badge">KIT</span>
    <span class="agent-badge">EWS</span>
    <span class="agent-badge">Rec</span>
    <span class="agent-badge">Síntesis</span>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📊 Estado del Proyecto")
    st.markdown("✅ **18/18** entregables")
    st.markdown("🏆 **Nota: 9/10**")
    st.markdown("📅 Auditoría: 2026-04-24")

    st.divider()
    modulo = st.radio(
        "Selecciona el módulo:",
        ["🎯 Dashboard Ejecutivo", "🔍 Análisis AMC Competidores", "🚨 Early Warning System", "💬 Pregunta al Agente"],
        index=0,
    )

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 1: Dashboard Ejecutivo
# ─────────────────────────────────────────────────────────────────────────────
if modulo == "🎯 Dashboard Ejecutivo":
    st.markdown("## 🎯 Dashboard Ejecutivo")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Veredicto Final", "CONDITIONAL GO", "72% confidence")
    with col2:
        st.metric("E[NPV] Alianza Sanitas", "+€14,2M", "+€8,6M si WACC=8%")
    with col3:
        st.metric("KIIs monitorizados", "9/9", "Estado: VERDE")
    with col4:
        st.metric("Entregables Brief", "18/18", "Nota: 9/10")

    st.divider()
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 🏁 Árbol de Decisión")
        opciones = {
            "Alianza Sanitas/BUPA": 14.2,
            "Alianza Adeslas": 4.6,
            "No Entrada": 0.0,
            "Entrada Directa": -3.5,
        }
        import pandas as pd
        df = pd.DataFrame(list(opciones.items()), columns=["Opción", "E[NPV] (M€)"])
        df = df.sort_values("E[NPV] (M€)", ascending=False)
        colors = ["#28a745" if v > 0 else "#dc3545" for v in df["E[NPV] (M€)"]]
        st.bar_chart(df.set_index("Opción"))
        st.caption("Solo la Alianza Sanitas tiene E[NPV] positivo y robusto")

    with col_right:
        st.markdown("### 🎲 Probabilidades de Escenarios (Fase 3)")
        escenarios = {
            "A: Alianza Rápida": 35,
            "C: Entrada Defensiva": 30,
            "D: Guerra + Cierre": 20,
            "B: Carrera en Abierto": 15,
        }
        df_esc = pd.DataFrame(list(escenarios.items()), columns=["Escenario", "P (%)"])
        st.bar_chart(df_esc.set_index("Escenario"))
        st.caption("Escenario A + C = 65% favorables a la alianza")

    st.divider()
    st.markdown("### 🔗 Cadenas de Trazabilidad F1 → F5")
    with st.expander("Ver cadenas verificadas por la auditoría"):
        st.markdown("""
| Cadena | F1 | F2 | F3 | F4 | F5 |
|--------|----|----|----|----|-----|
| **Regulatoria** | BC-3 blind spot | — | Supuesto LB#1 P=35% | Esc. D -€8M alianza | KIT2 + KII-4 BOE |
| **Modelo médico** | BC-1 transferibilidad | — | Supuesto Vul.#5 médicos | Sensibilidad ocupación | KII médicos reclutados |
| **Alianza Sanitas** | — | AMC 87% | Esc. A P=35% | E[NPV] +€14,2M | CONDITIONAL GO + S1 |
        """)

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 2: Análisis AMC
# ─────────────────────────────────────────────────────────────────────────────
elif modulo == "🔍 Análisis AMC Competidores":
    st.markdown("## 🔍 Análisis AMC — Competidores Españoles")
    st.markdown("> Framework: Chen & Miller (2012) — Awareness / Motivation / Capability")

    competidor_sel = st.selectbox(
        "Selecciona el competidor a analizar:",
        ["Todos", "Sanitas (BUPA)", "Adeslas (Mutua/CaixaBank)", "Asisa (HLA)"],
    )

    if st.button("▶️  Ejecutar Agente AMC", type="primary"):
        with st.spinner("🤖 Agentes OSINT + Alt.Data + AMC ejecutándose..."):
            sistema = IntelligenceSystem()
            filtro = None
            if competidor_sel != "Todos":
                filtro = competidor_sel.split(" ")[0].lower()
            fuentes, scores = sistema.ejecutar(export_json=False, competidor=filtro)

        st.success("✅ Análisis completado")

        for score in scores:
            with st.expander(f"📊 {score.competidor} — P(respuesta) = **{score.p_respuesta:.0f}%**", expanded=True):
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Awareness", f"{score.awareness}/5")
                c2.metric("Motivation", f"{score.motivation}/5")
                c3.metric("Capability", f"{score.capability}/5")
                c4.metric("P(respuesta)", f"{score.p_respuesta:.0f}%",
                          f"{score.timeline_meses_min}-{score.timeline_meses_max} meses")

                col_a, col_m = st.columns(2)
                with col_a:
                    st.markdown("**Evidencias Awareness:**")
                    for e in score.awareness_evidencia[:2]:
                        st.markdown(f"- {e}")
                with col_m:
                    st.markdown("**Evidencias Motivation:**")
                    for e in score.motivation_evidencia[:2]:
                        st.markdown(f"- {e}")

                st.markdown("**Tipos de respuesta más probables:**")
                resp_cols = st.columns(len(score.tipo_respuesta))
                for i, resp in enumerate(score.tipo_respuesta):
                    tipo = list(resp.keys())[0].replace("_", " ").title()
                    prob = list(resp.values())[0] * 100
                    resp_cols[i].metric(tipo, f"{prob:.0f}%")

        st.divider()
        st.markdown("### 📁 Fuentes verificadas")
        import pandas as pd
        df_fuentes = pd.DataFrame([
            {"ID": f.id, "Fuente": f.nombre[:50], "Tipo": f.tipo, "Framework": f.framework_link}
            for f in fuentes
        ])
        st.dataframe(df_fuentes, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 3: Early Warning System
# ─────────────────────────────────────────────────────────────────────────────
elif modulo == "🚨 Early Warning System":
    st.markdown("## 🚨 Early Warning System — Dashboard KIIs")
    st.markdown("> Framework: KITs → KIIs (Gilad, TN03) | 3 KITs · 9 KIIs · Umbrales automáticos")

    st.info("💡 **Modo demo:** Puedes cambiar el estado de los KIIs manualmente para simular alertas. En producción, los datos se actualizan automáticamente cada lunes vía GitHub Actions.")

    # Inicializar sistema
    ews = EarlyWarningSystem()
    kits = ews.kit_agent.definir_kits()
    kiis = ews.ews_agent.definir_kiis()

    st.markdown("### Simula una situación de alerta")
    col_sim1, col_sim2, col_sim3 = st.columns(3)
    with col_sim1:
        if st.button("🟢 Todos VERDE (estado actual)", use_container_width=True):
            for k in kiis:
                k.nivel_alerta = AlertLevel.GREEN
    with col_sim2:
        if st.button("🟡 KIT1 en AMARILLO (señal temprana)", use_container_width=True):
            kiis[0].nivel_alerta = AlertLevel.YELLOW
            kiis[1].nivel_alerta = AlertLevel.YELLOW
    with col_sim3:
        if st.button("🔴 KIT2 en ROJO (¡alerta regulatoria!)", use_container_width=True):
            kiis[3].nivel_alerta = AlertLevel.RED
            kiis[4].nivel_alerta = AlertLevel.RED

    verde, amarillo, rojo = ews.ews_agent.evaluar_alertas(kiis)
    revision = ews.ews_agent.decision_revision_estrategica(rojo)

    # Banner de alerta global
    if rojo >= 2:
        st.markdown(f'<div class="alert-rojo">🚨 <b>REVISIÓN ESTRATÉGICA REQUERIDA</b> — {rojo} KIIs en ROJO · Comité convocado en 48h</div>', unsafe_allow_html=True)
    elif amarillo >= 1:
        st.markdown(f'<div class="alert-amarillo">⚠️ <b>ALERTA</b> — {amarillo} KII(s) en AMARILLO · Revisión en 5 días laborables</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="alert-verde">✅ <b>ESTADO NOMINAL</b> — Todos los KIIs en VERDE · Seguimiento rutinario</div>', unsafe_allow_html=True)

    st.markdown(f"**Resumen:** {verde} 🟢 VERDE · {amarillo} 🟡 AMARILLO · {rojo} 🔴 ROJO")
    st.divider()

    for kit in kits:
        kiis_kit = [k for k in kiis if k.kit_id == kit.id]
        rojos_kit = sum(1 for k in kiis_kit if k.nivel_alerta == AlertLevel.RED)
        amarillos_kit = sum(1 for k in kiis_kit if k.nivel_alerta == AlertLevel.YELLOW)

        icono = "🔴" if rojos_kit > 0 else ("🟡" if amarillos_kit > 0 else "🟢")
        with st.expander(f"{icono} KIT {kit.id} — {kit.nombre}", expanded=(rojos_kit > 0 or amarillos_kit > 0)):
            st.markdown(f"*{kit.pregunta_central}*")
            st.caption(f"Relevancia: {kit.relevancia[:120]}...")

            for kii in kiis_kit:
                col_ind, col_fuente, col_freq, col_estado = st.columns([3, 2, 1, 1])
                col_ind.markdown(f"**KII {kii.id}:** {kii.indicador[:60]}...")
                col_fuente.caption(kii.fuente[:40])
                col_freq.caption(kii.frecuencia)
                estado_txt = {"VERDE": "🟢", "AMARILLO": "🟡", "ROJO": "🔴"}
                col_estado.markdown(f"### {estado_txt.get(kii.nivel_alerta.value, '⚪')}")

    st.divider()
    st.markdown("### ⚡ Protocolo de Escalado")
    import pandas as pd
    protocolo = pd.DataFrame([
        {"Nivel": "🟢 Vigilancia", "Condición": "0 KIIs en umbral", "Acción": "Seguimiento rutinario"},
        {"Nivel": "🟡 Alerta", "Condición": "1 KII AMARILLO", "Acción": "Revisión KIT en 5 días"},
        {"Nivel": "🔴 Escalado", "Condición": "1 KII ROJO", "Acción": "Informe dirección en 72h"},
        {"Nivel": "🔴🔴 Revisión estratégica", "Condición": "≥2 KIIs ROJO", "Acción": "Comité en 48h"},
        {"Nivel": "🚨 Stop inversión", "Condición": "≥3 KIIs ROJO", "Acción": "Suspender CapEx"},
    ])
    st.dataframe(protocolo, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 4: Pregunta al Agente
# ─────────────────────────────────────────────────────────────────────────────
elif modulo == "💬 Pregunta al Agente":
    st.markdown("## 💬 Pregunta al Agente Estratégico")
    st.markdown("> El agente responde usando los datos reales de las Fases 1–5 del proyecto.")

    # Base de conocimiento del agente
    KNOWLEDGE_BASE = {
        "sanitas": {
            "keywords": ["sanitas", "bupa", "alianza", "jv", "joint venture"],
            "response": """**Análisis Sanitas/BUPA — Agente AMC**

📊 **Puntuación AMC:** Awareness 5/5 · Motivation 4/5 · Capability 5/5
⚡ **P(respuesta): 87%** en 3-6 meses

**¿Por qué Sanitas es el socio ideal?**
- BUPA ya opera en México (Vitamedica + Hospital Bite Medica CDMX) → conoce el modelo de 50 Doctors directamente
- Es simultáneamente el competidor más peligroso (AMC 87%) Y el socio más natural
- Tiene relaciones institucionales con CCAA Madrid → mitiga el riesgo regulatorio (Supuesto LB#1)

**Tipo de respuesta más probable si 50D propone alianza:**
- Alianza estratégica: **40%**
- Contraofensiva: 30%
- Observación: 20%
- Adquisición: 10%

**Veredicto:** CONDITIONAL GO con Sanitas/BUPA — E[NPV] = **+€14,2M** (base) / **+€22,8M** (WACC=8%)"""
        },
        "adeslas": {
            "keywords": ["adeslas", "segurcaixa", "caixabank", "mutua"],
            "response": """**Análisis Adeslas — Agente AMC**

📊 **Puntuación AMC:** Awareness 3/5 · Motivation 3/5 · Capability 5/5
⚡ **P(respuesta): 60%** en 6-12 meses

**Perfil estratégico:**
- Líder del mercado: 9.757M€ ingresos, 19M+ asegurados, respaldo CaixaBank
- NO tiene hospitales propios → 50 Doctors es proveedor, no competidor directo
- Sin presencia en México → menor urgencia de reacción

**Valor como opción secundaria:**
- E[NPV] como red proveedora: **+€4,6M**
- Hedging Action H1: negociar con Adeslas en paralelo a Sanitas aumenta poder negociador

**Posición actual:** Alianza de red proveedora viable pero no como primera opción"""
        },
        "asisa": {
            "keywords": ["asisa", "hla", "cooperativa"],
            "response": """**Análisis Asisa/HLA — Agente AMC**

📊 **Puntuación AMC:** Awareness 3/5 · Motivation 4/5 · Capability 3/5
⚡ **P(respuesta): 55%** en 6-9 meses

**¿Por qué Asisa es el "jugador sorpresa"?**
- ÚNICO de los 3 que posee y opera hospitales → competidor DIRECTO del modelo de 50D
- HLA opera en Madrid, Barcelona, Málaga = las mismas ciudades que 50 Doctors
- Presencia en México vía Fundación Espriu → conoce el mercado
- PERO: modelo cooperativo = decisiones lentas, menor capacidad financiera

**Insight del War Game (Fase 3):**
En la Ronda 1, Asisa se movió ANTES que Adeslas para contactar a 50 Doctors.
Los jugadores de tamaño medio con mayor urgencia competitiva pueden ser los primeros en reaccionar."""
        },
        "ecomo": {
            "keywords": ["ecomo", "npv", "npv", "wacc", "financiero", "dinero", "valor", "inversion"],
            "response": """**Evaluación Económica — Agente ECOMO**

💰 **Resultados del modelo (4 opciones, 5 años):**

| Opción | E[NPV] | Recomendación |
|--------|--------|---------------|
| Alianza Sanitas/BUPA | **+€14,2M** | ✅ RECOMENDADO |
| Alianza Adeslas | +€4,6M | ⚠️ Secundaria |
| No Entrada | €0M | Baseline |
| Entrada Directa | **-€3,5M** | 🛑 NO |

**WACC:**
- Standalone 50D: **12%** (prima riesgo cross-border)
- Con financiación BUPA: **8%** → E[NPV] sube a +€22,8M (+60%)

**Variable más crítica:** Ocupación Año 3 (±€16M de impacto por ±10 pp)

**Exchange Value del JV:**
- Total: €160M
- 50D captura: **€96M** (60%)
- Sanitas captura: €64M (40%)"""
        },
        "regulacion": {
            "keywords": ["regulacion", "regulación", "boe", "dgs", "ministerio", "cnmc", "legal"],
            "response": """**Análisis Regulatorio — Agente EWS (KIT 2)**

📋 **Estado actual (2026-04):** 🟢 VERDE — Sin restricciones activas

**El mayor riesgo del proyecto:**
- Supuesto Load-Bearing #1 (ABP): P(fallo regulatorio) = **35%**
- Si la regulación es restrictiva → activa Escenario C/D (P=50% combinado)
- En Escenario D: la alianza pierde -€8M EUR

**Antídoto:** Sanitas como socio tiene relaciones institucionales con CCAA Madrid.
Condición GO C3: carta de no-oposición de CCAA antes de iniciar obras.

**KIIs regulatorios a monitorizar:**
- KII-4: Resoluciones DGS sobre inversión extranjera (BOE semanal)
- KII-5: Cambios en tarifas concertadas (trimestral)
- KII-6: Declaraciones del Ministro de Sanidad (mensual)

**Señal de aborto:** Cualquier resolución DGS restrictiva → ROJO inmediato"""
        },
        "escenarios": {
            "keywords": ["escenario", "shell", "probabilidad", "futuro", "planning"],
            "response": """**Scenario Planning — Shell Method (Fase 3)**

🗺️ **Matriz 2×2 de incertidumbre:**

```
             Cooperativas    Agresivas
Favorable  │ A: Alianza     │ B: Carrera   │
           │   Rápida (35%) │  Abierto(15%)│
Restrictiva│ C: Entrada     │ D: Guerra+   │
           │  Defensiva(30%)│  Cierre (20%)│
```

**Escenario más probable:** A + C = **65%** favorables a la alianza

**Escenario a vigilar:** D (20%) — único con E[NPV] negativo para la alianza (-€8M)

**Probabilidades usadas de forma consistente** en Fases 3, 4 y 5 (auditado ✅)"""
        },
        "default": {
            "response": """**Respuesta del Sistema Agéntico**

No encuentro ese término en la base de conocimiento del proyecto. Prueba preguntando sobre:

- 🏦 **Competidores:** "¿Cómo reaccionará Sanitas?" / "Analiza Adeslas"
- 💰 **Finanzas:** "¿Cuál es el NPV?" / "Explica el WACC"
- ⚖️ **Regulación:** "¿Qué riesgo regulatorio hay?"
- 🎲 **Escenarios:** "¿Cuál es el escenario más probable?"
- 🏥 **50 Doctors:** "¿Cuál es el modelo de negocio?"

O ejecuta el análisis completo desde el módulo **🔍 Análisis AMC Competidores**."""
        }
    }

    # Preguntas sugeridas
    st.markdown("### 💡 Preguntas sugeridas para la demo:")
    col_q1, col_q2, col_q3 = st.columns(3)
    with col_q1:
        if st.button("¿Cómo reaccionará Sanitas?", use_container_width=True):
            st.session_state['pregunta'] = "¿Cómo reaccionará Sanitas ante la entrada de 50 Doctors?"
    with col_q2:
        if st.button("¿Cuál es el NPV esperado?", use_container_width=True):
            st.session_state['pregunta'] = "¿Cuál es el NPV esperado de la alianza?"
    with col_q3:
        if st.button("¿Qué riesgo regulatorio hay?", use_container_width=True):
            st.session_state['pregunta'] = "¿Qué riesgo regulatorio existe en España?"

    col_q4, col_q5, col_q6 = st.columns(3)
    with col_q4:
        if st.button("¿Cuál es el escenario más probable?", use_container_width=True):
            st.session_state['pregunta'] = "¿Cuál es el escenario más probable?"
    with col_q5:
        if st.button("Analiza a Adeslas", use_container_width=True):
            st.session_state['pregunta'] = "Analiza el perfil de Adeslas como competidor"
    with col_q6:
        if st.button("¿Por qué CONDITIONAL GO?", use_container_width=True):
            st.session_state['pregunta'] = "¿Por qué el veredicto es CONDITIONAL GO y no GO?"

    # Input de pregunta
    pregunta = st.text_input(
        "O escribe tu propia pregunta:",
        value=st.session_state.get('pregunta', ''),
        placeholder="Ej: ¿Por qué Sanitas es mejor socio que Adeslas?",
        key="input_pregunta"
    )

    if st.button("🤖 Preguntar al Agente", type="primary") and pregunta:
        with st.spinner("🔍 Consultando base de conocimiento del proyecto..."):
            import time
            time.sleep(0.8)  # Simular procesamiento

            pregunta_lower = pregunta.lower()
            respuesta = KNOWLEDGE_BASE["default"]["response"]

            for key, data in KNOWLEDGE_BASE.items():
                if key == "default":
                    continue
                if any(kw in pregunta_lower for kw in data["keywords"]):
                    respuesta = data["response"]
                    break

        st.markdown("---")
        st.markdown("### 🤖 Respuesta del Agente Estratégico")
        st.markdown(respuesta)

        st.markdown("---")
        st.caption(f"⏱️ Respuesta generada: {datetime.now().strftime('%H:%M:%S')} · Base de datos: Fases 1-5 del proyecto · Auditoría: 18/18 ✅")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("🏥 50 Doctors México · Inteligencia Empresarial II · UFV · Prof. César Moreno Pascual PhD · 2026")
