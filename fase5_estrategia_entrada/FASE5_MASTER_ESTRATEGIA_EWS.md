# FASE 5 — EARLY WARNING SYSTEM + RECOMENDACIÓN ESTRATÉGICA FINAL
## 50 Doctors México — Expansión al Mercado Español de Salud

**Frameworks:** KITs → KIIs (Gilad, TN03) / Shaping & Hedging Actions (TN01/TN02) / ABP Signposts (TN02)
**Fecha:** 2026-04-22 | **Revisado:** 2026-04-25
**Estado:** 🟢 COMPLETADO
**Responsable:** Pablo Cerezal
**Sistema agéntico:** `agentic_ews_system.py` — 4 agentes (KIT, EWS, Rec, Síntesis)

> **Nota de unificación (2026-04-25):** Este documento es el maestro único de Fase 5, resultado de unificar FASE5_ESTRATEGIA_ENTRADA.md y FASE5_EARLY_WARNING_STRATEGIC_RECOMMENDATION.md. Incorpora los 9 KIIs del dashboard agéntico, el protocolo de escalado completo y las condiciones GO con KPIs verificables.

---

## RESUMEN EJECUTIVO

Basándose en el análisis acumulado de las Fases 1–4, se emite un **Conditional Go** con nivel de confianza del **72%** a favor de la alianza JV con Sanitas/BUPA. El Sistema de Alerta Temprana (EWS) monitoriza las tres variables de mayor carga estratégica (receptividad de aseguradoras, marco regulatorio y movimientos competitivos) con **9 indicadores clave (KIIs)**, umbrales de activación diferenciados (🟡 AMARILLO / 🔴 ROJO) y responsables asignados.

**Lógica de decisión:**
- E[NPV] Alianza Sanitas = **+€14,2M** → única opción con valor positivo y robusto
- Ventana de negociación = **3-6 meses** (AMC Sanitas P=87%)
- Acción inmediata requerida: CEO-to-CEO con Sanitas **antes de 90 días**

---

## SECCIÓN A — EARLY WARNING SYSTEM (EWS)

*Framework: KITs → KIIs (Gilad, TN03) + Weak Signal Detection*

---

### A.1 — Los 3 Key Intelligence Topics (KITs)

Los KITs operativizan los **supuestos load-bearing de la ABP (Fase 3)** y los **drivers de sensibilidad del ECOMO (Fase 4)**. Un cambio en cualquiera de ellos puede alterar el E[NPV] de la Alianza Sanitas en **±5–16M EUR**.

---

**KIT 1 — Receptividad de aseguradoras españolas a alianzas internacionales**

> *¿Está Sanitas/BUPA activamente dispuesta a co-invertir en un JV hospitalario con 50 Doctors en los próximos 6-12 meses?*

**Relevancia:** Supuesto crítico ABP #2 (P(fallo)=40%): si Sanitas rechaza el JV, el E[NPV] cae de +14,2M a -8M EUR — el mayor determinante de la decisión final. La ventana de negociación es estrecha: BUPA inauguró Hospital Blua Valdebebas (junio 2025) y puede priorizar expansión propia si 50 Doctors no actúa en los próximos 3-6 meses. Tipo de respuesta más probable según AMC: **alianza estratégica (40%)** si el enfoque es colaborativo.

**Señal de oportunidad detectada (Fase 2):** BUPA ya opera en México (Vitamedica, 7.500+ proveedores; Hospital Bite Medica CDMX, 2022). Conoce el mercado de 50 Doctors directamente → elimina asimetría de información en la negociación cross-border.

---

**KIT 2 — Cambios regulatorios en el sector sanitario privado español**

> *¿Introducirá la DGS o el Ministerio de Sanidad restricciones a la inversión extranjera en hospitales privados en 2026-2027?*

**Relevancia:** Supuesto crítico ABP #1 (P(fallo)=35%): regulación adversa activa el Escenario C/D (P=50% combinado). En Escenario D la alianza pierde -8M EUR — el único escenario con E[NPV] negativo para la alianza. El antídoto estructural es la presencia de Sanitas como socio local con relaciones institucionales consolidadas en CCAA Madrid. MUFACE renovado (2025-2027) reduce riesgo regulatorio a corto plazo.

**Señal positiva actual:** Sin restricciones activas (estado 2026-04); la UE impulsa libre mercado de servicios (Directiva de Servicios).

---

**KIT 3 — Movimientos competitivos de Sanitas/Adeslas hacia México/LATAM**

> *¿Está BUPA acelerando su expansión hospitalaria en México o LATAM de forma que reduzca su interés en 50 Doctors como socio?*

**Relevancia:** Supuesto crítico ABP #4 (P(fallo)=25%): si BUPA prefiere expansión propia en MX sobre el JV, 50 Doctors pierde su ventaja competitiva diferencial de **25M EUR** (Exchange Value, Fase 4). BUPA ya opera Vitamedica + Hospital Bite Medica (CDMX) — señal de que México es mercado prioritario para el grupo.

---

### A.2 — Monitoring Dashboard — 9 KIIs

| # | KIT | Indicador (KII) | Fuente | Frecuencia | Umbral de Alerta | Owner |
|---|-----|-----------------|--------|------------|-----------------|-------|
| 1 | KIT 1 | Job postings "international partnerships" o "hospital expansion LATAM" en LinkedIn Sanitas/BUPA | LinkedIn Jobs / Sales Navigator | Mensual | 🔴 >3 postings/30d \| 🟡 1-3 postings | Persona 2 |
| 2 | KIT 1 | Menciones prensa financiera sobre "alianza hospital mexicano" o "50 Doctors España" | Google Alerts + Factiva (El Economista, Expansión) | Diaria | 🔴 >2 menciones/semana \| 🟡 1 mención/semana | Persona 5 |
| 3 | KIT 1 | NPS / satisfacción clientes Sanitas y Adeslas — señal de vulnerabilidad que abre oportunidad de entrada premium | Trustpilot / Redacción Médica encuestas sectoriales | Trimestral | 🔴 Caída >5 puntos NPS \| 🟡 Caída 2-5 puntos | Persona 1 |
| 4 | KIT 2 | Nuevas resoluciones DGS sobre inversión extranjera en hospitales privados | BOE (boe.es) + DGSFP (dgsfp.mineco.gob.es) | Semanal | 🔴 Cualquier resolución restrictiva \| 🟡 Consulta pública abierta | Persona 5 |
| 5 | KIT 2 | Cambios en cobertura mínima seguros salud o tarifas concertadas (UNESPA/CCAA) | BOE / UNESPA / CCAA Madrid-Cataluña-Andalucía | Trimestral | 🔴 Cambio que afecte tarifas JV >10% \| 🟡 Consulta sobre tarifas | Persona 5 |
| 6 | KIT 2 | Declaraciones públicas del Ministro de Sanidad o Consejeros CCAA sobre hospitales extranjeros | MSCBS ruedas de prensa + Twitter/X oficial del Ministerio | Mensual | 🔴 Declaración hostil directa \| 🟡 Mención negativa en contexto político | Persona 3 |
| 7 | KIT 3 | Anuncios de apertura o adquisición de hospitales por Sanitas/BUPA en México o LATAM | CNMC + Prensa financiera + BUPA Group Press Releases | Mensual | 🔴 Nuevo hospital BUPA en MX (anuncio formal) \| 🟡 Exploración pública | Persona 2 |
| 8 | KIT 3 | Movimientos M&A de Adeslas o ASISA en México/LATAM (adquisiciones, JVs, acuerdos) | CNMC + Bloomberg + Latin Lawyer + Tracxn | Mensual | 🔴 JV competidor con rival directo de 50D en MX \| 🟡 Due diligence rumoreada | Persona 2 |
| 9 | KIT 3 | Resultados financieros BUPA ELA H1 2026 (revenue, guidance de expansión) | BUPA Group Half-Year Results (bupa.com/news-and-press) | Semestral | 🔴 Guidance expansión orgánica España >€100M sin socio \| 🟡 Menciones MX en guidance | Persona 2 |

**Estado actual (2026-04-25):** 9/9 KIIs en estado 🟢 VERDE — sin alertas activas.

> **Automatización:** El sistema agéntico `agentic_ews_system.py` genera este dashboard en tiempo real mediante `--check-alerts`. GitHub Actions ejecuta el sistema automáticamente cada lunes a las 08:00 y commitea el JSON de resultados al repositorio (ver `.github/workflows/ews-monitor.yml`).

---

### A.3 — Protocolo de Escalado

| Nivel de alerta | Condición de activación | Acción requerida |
|----------------|------------------------|-----------------|
| 🟢 **Vigilancia** | 0 KIIs en umbral | Seguimiento rutinario según frecuencias del dashboard |
| 🟡 **Alerta** | 1 KII 🟡 AMARILLO | Revisión del KIT afectado en 5 días laborables |
| 🔴 **Escalado** | 1 KII 🔴 ROJO | Revisión KIT + informe a dirección en 72h |
| 🔴🔴 **Revisión Estratégica** | ≥2 KIIs 🔴 ROJO | Comité de decisión convocado en 48h; posible renegociación de condiciones GO |
| 🚨 **Stop de inversión** | ≥3 KIIs 🔴 ROJO | Suspensión inmediata de compromisos de CapEx hasta nueva evaluación |

**Umbral crítico especial (KIT 2):** Cualquier resolución DGS restrictiva activa **directamente el nivel ROJO**, independientemente del estado del resto de KIIs. Es la señal de aborto más fiable del modelo.

---

## SECCIÓN B — RECOMENDACIÓN ESTRATÉGICA FINAL

*Framework: Go / No-Go / Conditional Go (TN01/TN02) + Shaping & Hedging Actions*

---

### B.1 — Veredicto

```
┌─────────────────────────────────────────────────────────────────────┐
│             ✅ CONDITIONAL GO — ALIANZA JV SANITAS/BUPA              │
│                     Confidence Level: 72%                            │
├─────────────────────┬───────────────────────────────────────────────┤
│ E[NPV] base         │ +€14,2M (+€22,8M si WACC=8%)                 │
│ Downside máximo     │ -€8M (vs. -€45M en entrada directa)           │
│ P(éxito escenarios) │ 80% (A+B+C combinados — Fase 3)              │
│ Variable crítica    │ Ocupación Año 3 ≥70% → garantía contractual   │
├─────────────────────┴───────────────────────────────────────────────┤
│ TRIGGER INMEDIATO   │ CEO-to-CEO con Sanitas en <90 días            │
│ SEÑAL DE ABORTO     │ KIT 2 activa nivel ROJO (resolución DGS)      │
│ SEÑAL DE ACELERAR   │ KIT 3 detecta movimiento BUPA/Sanitas en LATAM│
└─────────────────────────────────────────────────────────────────────┘
```

> El Confidence del 72% refleja: certeza metodológica alta sobre la superioridad de la alianza (E[NPV] robusto incluso si P(Escenario D) sube al 50% → +3,2M EUR) + incertidumbre moderada sobre la materialización exacta de los supuestos operativos (ocupación Año 3, regulación CCAA, WACC final de BUPA). No es GO incondicional porque las condiciones contractuales load-bearing no están firmadas todavía.

---

### B.2 — Top 3 Evidence Points

**[1] Superioridad financiera robusta de la alianza — Fase 4 (ECOMO / Decision Tree)**

La Alianza Sanitas/BUPA es la **única opción con E[NPV] positivo y significativo**: +14,2M EUR escenario-ponderado vs. Entrada Directa (-3,5M EUR) y No Entrada (0 EUR). La alianza mantiene E[NPV] positivo incluso si P(Escenario D, catastrófico) escala del 20% base al **50%** (+3,2M EUR) — robustez estructural demostrada. La asimetría del riesgo es definitiva: downside máximo de la alianza = **-€8M** vs. **-€45M** en entrada directa (reducción del **82% del riesgo catastrófico**). La inacción tiene un coste de oportunidad real de **14,2M EUR**.

*Peso: ALTO — métrica de decisión central*

---

**[2] BUPA ya opera en México y conoce el mercado de 50 Doctors — Fase 2 (AMC, Chen & Miller 2012)**

AMC Sanitas = 5/4/5, P(respuesta) = **87%**, timeline **3-6 meses**. BUPA Group opera activamente en México (Vitamedica, 7.500+ proveedores; Hospital Bite Medica CDMX). Conoce el modelo de 50 Doctors directamente → elimina la asimetría de información habitual en transacciones cross-border y acelera el due diligence. Tipo de respuesta más probable si 50D propone alianza: **alianza estratégica (40%)**. Esta ventana es temporal: si 50D no actúa en 6 meses, BUPA puede elegir expansión propia y el interés en el JV se enfría.

*Peso: ALTO — define la urgencia de la acción*

---

**[3] 50 Doctors captura 96M EUR de Exchange Value — Fase 4 (Exchange Value Framework)**

El modelo médico-socio, el pipeline LATAM y la velocidad de construcción generan **25M EUR de valor diferencial** que Sanitas no puede replicar sola. Exchange Value total del JV: **160M EUR** (50D: 96M, Sanitas: 64M). Si BUPA financia su 40% como deuda corporativa (WACC reducido al 8%), el E[NPV] de 50D escala de 14,2M a **22,8M EUR** (+60%). El poder negociador de 50D es real y cuantificable: **equity mínimo a negociar = 55%**.

*Peso: ALTO — justifica las condiciones contractuales del GO*

---

### B.3 — Condiciones para activar el GO

Deben cumplirse **antes de cualquier CapEx**:

| # | Condición | Responsable | Plazo | KPI verificable |
|---|-----------|-------------|-------|----------------|
| C1 | Sanitas compromete contractualmente derivación mínima del 20% de capacidad hospitalaria → garantiza ≥65% ocupación Año 3 (supuesto crítico ABP #3, P(fallo)=45%) | CEO 50D + Equipo Legal | 0-3 meses antes de CapEx | Cláusula de volumen garantizado en termsheet JV |
| C2 | BUPA Group financia su 40% como deuda corporativa (rating A), reduciendo WACC efectivo de 50D de 12% a 8-10%; E[NPV] sube de +14,2M a +22,8M EUR | CFO 50D + BUPA Group Treasury | 3-6 meses (cierre JV) | Termsheet de financiación con WACC efectivo <10% |
| C3 | Pre-acuerdo con autoridad sanitaria CCAA Madrid ANTES de iniciar obras, vía relaciones institucionales de Sanitas con Comunidad de Madrid | Sanitas (Rel. Institucionales) | 3-6 meses antes de CapEx | Carta de no-oposición / pre-autorización sanitaria CCAA Madrid |
| C4 | Cláusula de exit pactada: si Escenario D se materializa, BUPA tiene opción de compra del 60% de la JV a valor book → limita pérdida máxima 50D a **-€8M** | Legal 50D + M&A Advisor | En JV Agreement (6 meses) | Cláusula put firmada en JV Agreement |

---

### B.4 — Hedging Actions *(reducir exposición mientras se negocia)*

| # | Acción | Plazo | KPI |
|---|--------|-------|-----|
| H1 | Iniciar conversaciones paralelas con Adeslas como opción secundaria (E[NPV]=+4,6M EUR): posicionarse como proveedor de su red sin comprometer equity, manteniendo opcionalidad | 0-6 meses (simultáneo a Sanitas) | Carta de interés Adeslas como red proveedora (no vinculante) |
| H2 | Presupuestar 2-3M EUR en due diligence regulatoria y legal ANTES de comprometer CapEx: contratar asesor M&A español (Rothschild, KPMG Deal Advisory, Garrigues) | Primeros 3 meses | Informe DD entregado antes del termsheet |
| H3 | Estructurar JV con piloto de 1 hospital (H1 Madrid) antes de comprometer los 4 hospitales: limita exposición máxima a 17M EUR en Año 0 | Decisión en JV Agreement (6 meses) | Cláusula de expansión escalonada: H2 sujeta a 60% ocupación H1 en Año 2 |

---

### B.5 — Shaping Actions *(influir en el entorno a favor de 50 Doctors)*

| # | Acción | Plazo | KPI |
|---|--------|-------|-----|
| S1 | CEO 50D propone alianza formal a CEO Sanitas/BUPA ANTES de cualquier anuncio público en España: aprovechar la ventana AMC de 3-6 meses. Exchange Value diferencial (+25M EUR) otorga poder para exigir 55-65% del equity | Inmediato (primeros 30 días) | Reunión C-suite Sanitas/BUPA celebrada y minutes documentados |
| S2 | Activar red de turismo médico México-España: publicar casos de éxito de pacientes BUPA atendidos en 50D MX para demostrar pipeline de valor diferencial de 12M EUR/año antes del termsheet | 3-6 meses (previo al termsheet) | Informe de flujo de pacientes BUPA-MX → 50D (últimos 12 meses) |
| S3 | Participar como ponente en Foro Nacional de Sanidad Privada (FNSP) y congreso UNESPA 2026: posicionar 50D como referente del modelo médico-socio ante la comunidad aseguradora y regulatoria española | 6-12 meses | Invitación a ponencia aceptada + 3+ reuniones bilaterales post-evento |
| S4 | Reclutar 30-50 médicos mexicanos especializados en España mediante contratos de largo plazo: neutraliza el argumento político de "competencia desleal al SNS" y genera goodwill regulatorio | 6-12 meses | Contratos firmados + comunicado conjunto con Colegio de Médicos |

---

## CHECKLIST DE ENTREGABLES — VERIFICACIÓN FINAL

- [x] **3 KITs definidos** (KIT1: Receptividad aseguradoras, KIT2: Regulación, KIT3: Movimientos LATAM)
- [x] **Dashboard con 9 KIIs** (≥6 requerido) — fuente, frecuencia, umbral 🟡/🔴, owner para cada uno
- [x] **Veredicto CONDITIONAL GO con confidence 72%** — justificado con ECOMO + Decision Tree + ABP
- [x] **Top 3 evidence points** — E[NPV]+14,2M / AMC Sanitas 87% / Exchange Value 96M a favor 50D
- [x] **4 Condiciones GO** contractuales load-bearing con KPIs verificables
- [x] **3 Hedging Actions** (H1: Adeslas paralelo / H2: DD legal / H3: piloto 1 hospital)
- [x] **4 Shaping Actions** (S1: CEO-to-CEO / S2: turismo médico / S3: FNSP / S4: médicos)
- [x] **Sistema agéntico** — `agentic_ews_system.py` con 4 agentes + CLI + JSON export
- [x] **GitHub Actions** — ejecución automática semanal del EWS (`.github/workflows/ews-monitor.yml`)

---

## TRAZABILIDAD ENTRE FASES

| Cadena | F1 → F2 → F3 → F4 → F5 |
|--------|------------------------|
| **Regulatoria** | BC-3 (blind spot estructural) → Supuesto LB #1 (P=35%) → Esc. D (-8M alianza) → KIT 2 + KII-4 BOE/CNMC |
| **Modelo médico** | BC-1 (transferibilidad) → Supuesto Vul. #5 (médicos ES) → Sensibilidad ocupación → KII Médicos reclutados |
| **Alianza Sanitas** | AMC 87% → Esc. A (35%) → E[NPV] +14,2M EUR → CONDITIONAL GO + S1 CEO-to-CEO |

---

*Frameworks aplicados: KITs → KIIs (Gilad, TN03) | Early Warning / Weak Signals (TN03) | Shaping & Hedging Actions (TN01/TN02) | ABP Signposts (TN02)*
*Datos de fases previas: AMC Fase 2, Escenarios Shell Fase 3, ECOMO/Exchange Value Fase 4*
*Sistema agéntico ejecutado el 2026-04-25 — outputs en `resultados_ews_fase5.json`*

**Fecha completado:** 2026-04-22 | **Fecha revisión:** 2026-04-25
