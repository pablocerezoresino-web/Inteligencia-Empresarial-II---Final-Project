# Data Collection — Mapa de Fuentes (Fase 2)

**Estado:** 🟡 En progreso
**Última actualización:** 2026-04-21

---

## Tabla de Fuentes (8+ requeridas)

| # | Fuente | Tipo | Lead Time | Framework link | Estado | Evidencia recogida |
|---|--------|------|-----------|---|--------|---|
| 1 | **CNMC** — Informes Sanidad | Primaria/Pública | 1 mes | Capability | 🟡 Recogiendo | [En progreso] |
| 2 | **LinkedIn Job Postings** — Sanitas | Alt. Data | Tiempo real | Motivation | 🟡 Recogiendo | [En progreso] |
| 3 | **LinkedIn Job Postings** — Adeslas | Alt. Data | Tiempo real | Motivation | 🟡 Recogiendo | [En progreso] |
| 4 | **LinkedIn Job Postings** — Asisa | Alt. Data | Tiempo real | Motivation | 🟡 Recogiendo | [En progreso] |
| 5 | **Webs corporativas** — Sanitas/Adeslas/Asisa | OSINT | 1-2 días | Awareness | 🟡 Recogiendo | [En progreso] |
| 6 | **BOE** — Licitaciones sanitarias | Primaria/Pública | 1 mes | Capability | 🟡 Recogiendo | [En progreso] |
| 7 | **Noticias prensa** — Expansión competidores | Primaria | 1-2 semanas | Motivation/Awareness | 🟡 Recogiendo | [En progreso] |
| 8 | **Registro Mercantil** — Estructura accionarial | OSINT | 2 semanas | Capability | 🟡 Recogiendo | [En progreso] |

---

## Agentes de Recopilación (Agentic System)

### Agent 1 — OSINT Collector
**Objetivo:** Recopilar datos públicos estructurados
- CNMC: informes, estadísticas aseguradoras
- Registro Mercantil: estructura, directorios
- BOE: licitaciones, cambios normativos
- Webs corporativas: estructura, ofertas, números

### Agent 2 — Alternative Data Collector
**Objetivo:** Buscar señales débiles e indicadores de movimiento
- LinkedIn: job postings, crecimiento headcount, expansión geográfica
- Noticias: acuerdos, fusiones, alianzas, estrategia
- SimilarWeb: tráfico web, engagement
- ICEX/AEPD: regulación, cambios

### Agent 3 — AMC Analyzer
**Objetivo:** Generar puntuaciones A/M/C basadas en evidencia
- Analiza datos recogidos por Agentes 1 y 2
- Asigna puntuaciones 1-5 justificadas
- Estima P(respuesta) y timeline

---

## Notas de Compliance
- ✅ GDPR compliant: solo datos públicos (OSINT / alternative data legal)
- ✅ SCIP Code of Ethics: no competencia desleal, no datos robados
- ✅ Mantener trail de fuentes para auditoría

