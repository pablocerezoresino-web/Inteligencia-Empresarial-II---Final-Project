# Inteligencia Empresarial II — Proyecto Final
**Universidad Francisco de Vitoria | Profesor: César Moreno Pascual PhD**
**Auditoría:** 18/18 entregables cubiertos — **Nota global: 9/10** *(Pablo Cerezal, 2026-04-24)*

---

## La Empresa: 50 Doctors México → ¿Expansión a España?

**50 Doctors** (*Fifty Doctors*) es la cadena hospitalaria de mayor crecimiento en México. Su propuesta de valor combina infraestructura de lujo (5 estrellas) con precios accesibles para la clase media-alta, a través de un modelo único: los **50 mejores especialistas de cada ciudad son co-propietarios del hospital** (50% del capital). Esto alinea incentivos, elimina la dependencia de marketing y garantiza ocupación desde el día 1.

- **Fundadores:** Javier de Lope Francés (presidente), Jorge Marcos Martínez (DG)
- **Presencia 2026:** Puebla (2 sedes), Torreón, La Paz BCS, Cancún (1.750M MXN) + 14 hospitales en desarrollo
- **Meta:** 50 hospitales en México + primera expansión internacional → **Madrid, Barcelona, La Coruña, Málaga (~2027-2028)**
- **Reto de este proyecto:** ¿Con quién entrar en España? ¿Alianza con Sanitas/BUPA, Adeslas, entrada directa, o no entrar?

---

## Narrativa Ejecutiva End-to-End

### F1 → F2 → F3 → F4 → F5: Cómo llegamos a CONDITIONAL GO

**Fase 1** identifica el modelo de negocio y detecta 3 puntos ciegos críticos (Zahra & Chaples 1993): la asunción de que el modelo médico-socio es directamente exportable a España, la infravaloración de Quirónsalud como barrera competitiva, y la subestimación del ciclo regulatorio autonómico (24-36 meses). El Pre-Mortem (Klein) anticipa los tres caminos más probables hacia el fracaso.

**Fase 2** despliega un sistema agéntico de 4 agentes (OSINT + Alt.Data + AMC + Síntesis) sobre el mercado español. El hallazgo crítico: **BUPA ya opera en México** (Vitamedica, Hospital Bite Medica CDMX) y conoce el modelo de 50 Doctors directamente. Puntuaciones AMC: Sanitas 87% / P(respuesta) en 3-6 meses; Adeslas 60% en 6-12 meses; Asisa 55% en 6-9 meses. Sanitas es simultáneamente el competidor más peligroso y el socio más natural.

**Fase 3** aplica el Shell Method para construir la matriz 2×2 de incertidumbre (Eje X: regulación, Eje Y: respuesta aseguradoras) y genera 4 escenarios: **A** Alianza Rápida (P=35%), **B** Carrera en Abierto (P=15%), **C** Entrada Defensiva (P=30%), **D** Guerra + Cierre (P=20%). El War Game (3 equipos: Red/Blue/Green, 3 rondas, 2 shock events) prueba la estrategia bajo presión. La ABP identifica 5 supuestos críticos con sus signposts y acciones de shaping/hedging.

**Fase 4** cuantifica el valor económico de cada opción con el framework ECOMO + Exchange Value. Resultado: la Alianza Sanitas/BUPA es la única con E[NPV] positivo (+€14,2M). La Entrada Directa destruye valor esperado (-€3,5M). El Exchange Value total del JV asciende a €160M, de los cuales 50 Doctors captura **€96M** gracias a su ventaja diferencial. El análisis de sensibilidad revela que la variable más crítica es la ocupación del Año 3 (±€16M de impacto).

**Fase 5** integra todo en una recomendación ejecutiva accionable: **CONDITIONAL GO** (72% confidence) con 4 condiciones contractuales load-bearing, un Early Warning System de 9 KIIs monitorizando 3 KITs, y acciones de shaping (S1-S4) y hedging (H1-H3). El sistema agéntico EWS (`agentic_ews_system.py`) ejecuta el dashboard automáticamente cada semana vía GitHub Actions.

---

## Veredicto Final

```
┌────────────────────────────────────────────────────────────────────┐
│          ✅ CONDITIONAL GO — ALIANZA JV SANITAS/BUPA               │
│                   Confidence Level: 72%                             │
├────────────────────────┬───────────────────────────────────────────┤
│ E[NPV] Alianza Sanitas │ +€14,2M base → +€22,8M (WACC=8%)        │
│ E[NPV] Entrada Directa │ -€3,5M  ← NO RECOMENDADO                │
│ Exchange Value 50D     │ €96M de €160M totales del JV             │
│ Ventana de acción      │ 3-6 meses (AMC Sanitas P=87%)            │
│ Variable crítica       │ Ocupación Año 3 ≥70% (±€16M impacto)    │
├────────────────────────┴───────────────────────────────────────────┤
│ ACCIÓN INMEDIATA       │ CEO-to-CEO con Sanitas en <90 días       │
│ SEÑAL DE ABORTO        │ Resolución DGS restrictiva → KIT 2 ROJO  │
└────────────────────────────────────────────────────────────────────┘
```

---

## Estructura del Repositorio

```
📁 Inteligencia-Empresarial-II---Final-Project/
│
├── 📄 README.md                          ← Este archivo (narrativa ejecutiva)
├── 📄 STATUS.md                          ← Estado del proyecto por fases
│
├── 📁 fase1_analisis_50doctors/
│   ├── analisis_fase1.md                 ← Canvas visual + DAFO + Competitive Repertoire
│   └── FASE1_BLIND_SPOT_CHECK.md         ← 3 Blind Spots (Zahra & Chaples) + Pre-Mortem
│
├── 📁 fase2_inteligencia_mercado_espanol/
│   ├── agentic_intelligence_system.py    ← Sistema agéntico (OSINT+AltData+AMC+Síntesis)
│   ├── RESULTADOS_FASE2.md               ← AMC Sanitas 87% / Adeslas 60% / Asisa 55%
│   ├── 03_evidencia_competidores.md      ← 12 fuentes verificadas con URLs
│   └── resultados_amc.json               ← Output JSON del sistema agéntico (evidencia)
│
├── 📁 fase3_war_gaming/
│   └── FASE3_WAR_GAMING_COMPLETO.md      ← Shell 2×2 + 4 Escenarios + War Game + ABP
│
├── 📁 fase4_evaluacion_economica/
│   ├── FASE4_ECOMO_EVALUACION_ECONOMICA.md ← Exchange Value + ECOMO NPV + Sensibilidad
│   └── FASE4_ECOMO_FORMULAS_ANEXO.md     ← Fórmulas explícitas y WACC breakdown
│
├── 📁 fase5_estrategia_entrada/
│   ├── FASE5_MASTER_ESTRATEGIA_EWS.md    ← Documento maestro F5 (KITs+KIIs+GO+Shaping)
│   ├── agentic_ews_system.py             ← Sistema agéntico EWS (4 agentes + CLI)
│   └── resultados_ews_fase5.json         ← Output JSON del EWS (evidencia de ejecución)
│
├── 📁 .github/workflows/
│   └── ews-monitor.yml                   ← GitHub Actions: EWS automático cada lunes
│
└── 📁 docs/
    ├── TN01_Strategic_Intelligence_v2.pdf
    ├── TN02_War_Gaming_Scenario_Planning.pdf
    ├── TN03_Blind_Spots_Alternative_Data.pdf
    ├── TN04_Defense_Cyber.pdf
    ├── TN05_Financial_Services_v2.pdf
    └── TN10_Agentic_Foundations_MultiAgent.pdf
```

---

## Sistemas Agénticos — Cómo Ejecutarlos

### Sistema F2 — Inteligencia Competitiva AMC
```bash
# Análisis completo de los 3 competidores
py fase2_inteligencia_mercado_espanol/agentic_intelligence_system.py

# Filtrar por competidor específico
py fase2_inteligencia_mercado_espanol/agentic_intelligence_system.py --competidor sanitas

# Exportar resultados a JSON
py fase2_inteligencia_mercado_espanol/agentic_intelligence_system.py --export json
```

### Sistema F5 — Early Warning System
```bash
# Dashboard completo con informe ejecutivo
py fase5_estrategia_entrada/agentic_ews_system.py

# Solo estado de alertas (rápido, para monitoreo diario)
py fase5_estrategia_entrada/agentic_ews_system.py --check-alerts

# Solo veredicto estratégico
py fase5_estrategia_entrada/agentic_ews_system.py --recommendation-only

# Exportar dashboard a JSON
py fase5_estrategia_entrada/agentic_ews_system.py --export json
```

> **Automatización:** el workflow `.github/workflows/ews-monitor.yml` ejecuta el EWS automáticamente cada lunes a las 08:00 UTC y actualiza `resultados_ews_fase5.json` en el repositorio.

---

## Cadenas de Trazabilidad (Auditadas)

| Cadena | F1 → F2 → F3 → F4 → F5 |
|--------|------------------------|
| **Regulatoria** | BC-3 (blind spot) → Supuesto LB#1 P=35% → Esc. D -€8M → KIT2 + KII-4 BOE |
| **Modelo médico** | BC-1 (transferibilidad) → Supuesto Vul.#5 → Sensibilidad ocupación → KII médicos |
| **Alianza Sanitas** | AMC 87% → Esc. A 35% → E[NPV] +€14,2M → CONDITIONAL GO + S1 CEO-to-CEO |

---

## Equipo y Estado del Proyecto

| Fase | Responsable | Estado | Nota auditoría |
|------|-------------|--------|----------------|
| F1 — Análisis 50 Doctors | Pablo Cerezal | 🟢 Completado | 8,5/10 |
| F2 — Inteligencia Mercado Español | Adrián | 🟢 Completado | 9/10 |
| F3 — War Gaming | Adrián | 🟢 Completado | 9,5/10 |
| F4 — Evaluación Económica | Adrián | 🟢 Completado | 9/10 |
| F5 — Estrategia + Early Warning | Pablo Cerezal | 🟢 Completado | 8,5/10 |
| **GLOBAL** | | 🟢 **APTO** | **9/10** |

Ver [STATUS.md](STATUS.md) para el log completo del proyecto.

---

## Cómo Trabajar en Este Repo
```bash
git pull origin main          # Siempre antes de empezar
# Trabaja en la carpeta de tu fase
git add <archivos>
git commit -m "Fase X: descripción"
git push origin main
```

*Proyecto completado — Auditoría final: 18/18 entregables Brief §3.1 cubiertos*
*Universidad Francisco de Vitoria · Inteligencia Empresarial II · 2026*
