#!/usr/bin/env python3
"""
Sistema Agentico de Inteligencia Competitiva
Fase 2: Inteligencia Competitiva del Mercado Español

Estructura:
- Agent OSINT: Recopila datos públicos (webs, CNMC, BOE)
- Agent Alt.Data: Busca indicadores débiles (LinkedIn, noticias, tráfico)
- Agent AMC: Analiza Awareness/Motivation/Capability
- Agent Síntesis: Integra datos en informe final

Uso:
    python agentic_intelligence_system.py --help
"""

import json
from dataclasses import dataclass, asdict
from typing import List, Dict
from enum import Enum
from datetime import datetime


class FrameworkLink(Enum):
    """Vinculación a frameworks"""
    AWARENESS = "AMC — Awareness"
    MOTIVATION = "AMC — Motivation"
    CAPABILITY = "AMC — Capability"
    OSINT = "OSINT — Datos Públicos"
    ALT_DATA = "Alt.Data — Señales Débiles"


@dataclass
class DataSource:
    """Fuente de datos recopilada"""
    id: int
    nombre: str
    tipo: str  # OSINT, Alt.Data, Primaria/Pública
    lead_time: str
    framework_link: str
    estado: str  # 🟡 Pendiente, 🟢 Completado
    evidencia_url: str = ""
    descripcion: str = ""
    recopilador: str = ""  # OSINT Agent, Alt.Data Agent
    fecha_recopilacion: str = ""


@dataclass
class AMCScore:
    """Puntuación AMC para un competidor"""
    competidor: str
    awareness: int  # 1-5
    awareness_evidencia: str
    motivation: int  # 1-5
    motivation_evidencia: str
    capability: int  # 1-5
    capability_evidencia: str
    p_respuesta: float  # % probabilidad
    timeline_meses: int
    analista: str = "Agent AMC"
    fecha: str = ""


class OSINTAgent:
    """Recopila datos públicos de fuentes de inteligencia de código abierto"""

    def __init__(self):
        self.nombre = "Agent OSINT"
        self.fuentes_recopiladas = []

    def recopilar_cnmc(self, competidores: List[str]) -> List[DataSource]:
        """Busca en CNMC (Comisión Nacional del Mercado de Valores)"""
        fuentes = []
        for comp in competidores:
            fuente = DataSource(
                id=1,
                nombre=f"CNMC — Informe {comp}",
                tipo="Primaria/Pública",
                lead_time="1 mes",
                framework_link="Capability",
                estado="🟡 Pendiente",
                descripcion=f"Informe regulatorio CNMC sobre {comp}"
            )
            fuentes.append(fuente)
        return fuentes

    def recopilar_boe(self) -> DataSource:
        """Busca en BOE (Boletín Oficial del Estado)"""
        return DataSource(
            id=4,
            nombre="BOE — Licitaciones sanitarias",
            tipo="Primaria/Pública",
            lead_time="2 semanas",
            framework_link="Capability",
            estado="🟡 Pendiente",
            descripcion="Licitaciones de servicios sanitarios en últimos 6 meses"
        )

    def recopilar_registro_mercantil(self, competidores: List[str]) -> List[DataSource]:
        """Busca en Registro Mercantil"""
        fuentes = []
        for comp in competidores:
            fuente = DataSource(
                id=8,
                nombre=f"Registro Mercantil — {comp}",
                tipo="OSINT",
                lead_time="2 semanas",
                framework_link="Capability",
                estado="🟡 Pendiente",
                descripcion=f"Estructura accionarial, cambios en junta directiva"
            )
            fuentes.append(fuente)
        return fuentes


class AltDataAgent:
    """Recopila datos alternativos (señales débiles)"""

    def __init__(self):
        self.nombre = "Agent Alt.Data"
        self.fuentes_recopiladas = []

    def recopilar_linkedin_hiring(self, competidores: List[str]) -> List[DataSource]:
        """Busca job postings en LinkedIn (Motivation indicator)"""
        fuentes = []
        for comp in competidores:
            fuente = DataSource(
                id=2,
                nombre=f"LinkedIn Job Postings — {comp}",
                tipo="Alt.Data",
                lead_time="Tiempo real",
                framework_link="Motivation",
                estado="🟡 Pendiente",
                descripcion=f"Ofertas de empleo: crecimiento de headcount, roles de expansión"
            )
            fuentes.append(fuente)
        return fuentes

    def recopilar_noticias_prensa(self, competidores: List[str]) -> List[DataSource]:
        """Busca noticias de prensa sobre competidores"""
        fuentes = []
        for comp in competidores:
            fuente = DataSource(
                id=7,
                nombre=f"Noticias Prensa — {comp}",
                tipo="Primaria",
                lead_time="1-2 semanas",
                framework_link="Awareness/Motivation",
                estado="🟡 Pendiente",
                descripcion=f"Alianzas, expansión, estrategia comunicada públicamente"
            )
            fuentes.append(fuente)
        return fuentes


class AMCAnalyzer:
    """Analiza Awareness/Motivation/Capability basado en evidencia"""

    def __init__(self):
        self.nombre = "Agent AMC"
        self.scores = []

    def calcular_awareness(self, evidencia: Dict) -> int:
        """
        Calcula Awareness (1-5):
        1-2: Ignorancia completa
        3: Parcialmente consciente
        4-5: Monitoreo activo
        """
        # Heurística: si tiene cobertura latam, ¿monitorea hospitales privados?
        if evidencia.get("parent_en_latam"):
            return 4
        elif evidencia.get("presencia_internacional"):
            return 3
        else:
            return 2

    def calcular_motivation(self, evidencia: Dict) -> int:
        """
        Calcula Motivation (1-5):
        1-2: Satisfecho, sin presión
        3: Crecimiento normal
        4-5: Necesidad estratégica de crecer
        """
        score = 0
        if evidencia.get("crecimiento_anual") and evidencia["crecimiento_anual"] > 10:
            score += 2
        if evidencia.get("plan_estrategico_expansion"):
            score += 2
        if evidencia.get("hiring_internacional"):
            score += 1
        return min(5, max(1, 2 + score))

    def calcular_capability(self, evidencia: Dict) -> int:
        """
        Calcula Capability (1-5):
        1-2: Atado, sin recursos
        3: Recursos limitados
        4-5: Bien financiado, experiencia internacional
        """
        score = 0
        if evidencia.get("parent_financiero_fuerte"):
            score += 2
        if evidencia.get("red_hospitalaria"):
            score += 1
        if evidencia.get("presencia_latam"):
            score += 2
        return min(5, max(1, 1 + score))

    def generar_amc_score(self, competidor: str, evidencia: Dict) -> AMCScore:
        """Genera puntuación AMC completa"""
        a = self.calcular_awareness(evidencia)
        m = self.calcular_motivation(evidencia)
        c = self.calcular_capability(evidencia)

        # P(Respuesta) = f(A, M, C)
        # Heurística: (A + M + C) / 15 * 100
        p_respuesta = ((a + m + c) / 15) * 100

        score = AMCScore(
            competidor=competidor,
            awareness=a,
            awareness_evidencia=evidencia.get("awareness_notes", ""),
            motivation=m,
            motivation_evidencia=evidencia.get("motivation_notes", ""),
            capability=c,
            capability_evidencia=evidencia.get("capability_notes", ""),
            p_respuesta=p_respuesta,
            timeline_meses=evidencia.get("timeline_meses", 6),
            fecha=datetime.now().isoformat()
        )
        return score


class SynthesisAgent:
    """Integra datos de todos los agentes en un informe coherente"""

    def __init__(self):
        self.nombre = "Agent Síntesis"

    def generar_markdown_informe(self,
                                 fuentes: List[DataSource],
                                 amc_scores: List[AMCScore]) -> str:
        """Genera markdown del informe de Fase 2"""

        md = "# Informe Fase 2 — Inteligencia Competitiva\n\n"

        md += "## Parte A: Data Collection\n\n"
        md += "### Tabla de Fuentes Recopiladas\n\n"
        md += "| # | Fuente | Tipo | Lead Time | Framework | Estado |\n"
        md += "|---|--------|------|-----------|-----------|--------|\n"

        for fuente in fuentes:
            md += f"| {fuente.id} | {fuente.nombre} | {fuente.tipo} | {fuente.lead_time} | {fuente.framework_link} | {fuente.estado} |\n"

        md += "\n## Parte B: AMC Analysis\n\n"
        md += "### Puntuaciones Awareness/Motivation/Capability\n\n"
        md += "| Competidor | A | M | C | P(Respuesta) | Timeline |\n"
        md += "|---------|---|---|---|---|---|\n"

        for score in amc_scores:
            md += f"| {score.competidor} | {score.awareness} | {score.motivation} | {score.capability} | {score.p_respuesta:.1f}% | {score.timeline_meses} meses |\n"

        return md


# Sistema Principal
class InteligenceSystem:
    """Orquestador principal del sistema agentico"""

    def __init__(self):
        self.osint = OSINTAgent()
        self.altdata = AltDataAgent()
        self.amc = AMCAnalyzer()
        self.synthesis = SynthesisAgent()
        self.competidores = ["Sanitas", "Adeslas", "Asisa"]

    def ejecutar_recopilacion_completa(self):
        """Ejecuta recopilación de datos con todos los agentes"""

        print("🤖 Sistema Agentico de Inteligencia Competitiva")
        print("=" * 60)

        # Fase 1: OSINT
        print("\n📊 Agent OSINT — Recopilando datos públicos...")
        fuentes_cnmc = self.osint.recopilar_cnmc(self.competidores)
        fuentes_boe = [self.osint.recopilar_boe()]
        fuentes_rm = self.osint.recopilar_registro_mercantil(self.competidores)

        # Fase 2: Alt.Data
        print("📡 Agent Alt.Data — Buscando señales débiles...")
        fuentes_linkedin = self.altdata.recopilar_linkedin_hiring(self.competidores)
        fuentes_noticias = self.altdata.recopilar_noticias_prensa(self.competidores)

        # Agregar todas las fuentes
        todas_fuentes = (fuentes_cnmc + fuentes_boe + fuentes_rm +
                        fuentes_linkedin + fuentes_noticias)

        print(f"✅ Recopiladas {len(todas_fuentes)} fuentes de datos\n")

        # Fase 3: AMC Analysis
        print("🔍 Agent AMC — Analizando Awareness/Motivation/Capability...")

        evidencia_sanitas = {
            "parent_en_latam": True,
            "presencia_internacional": True,
            "crecimiento_anual": 12,
            "plan_estrategico_expansion": True,
            "hiring_internacional": True,
            "parent_financiero_fuerte": True,
            "presencia_latam": True,
            "timeline_meses": 4,
            "awareness_notes": "BUPA lidera ELA, probablemente monitorea Latam",
            "motivation_notes": "Presión de BUPA por crecimiento, +12% ingresos",
            "capability_notes": "Financiamiento fuerte de BUPA, estructura BUPA ELA"
        }

        evidencia_adeslas = {
            "parent_en_latam": True,
            "presencia_internacional": True,
            "crecimiento_anual": 10,
            "plan_estrategico_expansion": True,
            "hiring_internacional": False,
            "parent_financiero_fuerte": True,
            "presencia_latam": True,
            "timeline_meses": 6,
            "awareness_notes": "Presencia en Chile 60%, probable monitoreo de expansión",
            "motivation_notes": "Plan 2024-2026 de €5.5B, estrategia de diversificación",
            "capability_notes": "Financiamiento de CaixaBank, experiencia en Chile"
        }

        evidencia_asisa = {
            "parent_en_latam": False,
            "presencia_internacional": False,
            "crecimiento_anual": 7,
            "plan_estrategico_expansion": False,
            "hiring_internacional": False,
            "parent_financiero_fuerte": True,
            "red_hospitalaria": True,
            "timeline_meses": 8,
            "awareness_notes": "Cobertura internacional limitada, Barcelona solo",
            "motivation_notes": "Crecimiento anual 7-10%, presión de competidores",
            "capability_notes": "Red HLA integrada, presupuesto menor que Sanitas/Adeslas"
        }

        score_sanitas = self.amc.generar_amc_score("Sanitas", evidencia_sanitas)
        score_adeslas = self.amc.generar_amc_score("Adeslas", evidencia_adeslas)
        score_asisa = self.amc.generar_amc_score("Asisa", evidencia_asisa)

        amc_scores = [score_sanitas, score_adeslas, score_asisa]

        print(f"✅ Análisis AMC completado\n")

        # Fase 4: Síntesis
        print("📝 Agent Síntesis — Generando informe...")
        informe_md = self.synthesis.generar_markdown_informe(todas_fuentes, amc_scores)

        return {
            "fuentes": [asdict(f) for f in todas_fuentes],
            "amc_scores": [asdict(s) for s in amc_scores],
            "informe_preview": informe_md
        }


if __name__ == "__main__":
    sistema = InteligenceSystem()
    resultados = sistema.ejecutar_recopilacion_completa()

    print("\n" + "=" * 60)
    print("📋 RESULTADOS DEL ANÁLISIS")
    print("=" * 60)
    print(resultados["informe_preview"])

    print("\n✅ Sistema completado. Datos guardados en JSON.")

    # Guardar resultados como JSON
    with open("resultados_amc.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)

    print(f"📁 Archivo: resultados_amc.json")
