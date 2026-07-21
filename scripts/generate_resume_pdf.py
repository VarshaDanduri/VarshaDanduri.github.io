#!/usr/bin/env python3
"""Generate Varsha Danduri resume PDF for GitHub Pages."""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "resume" / "Varsha_Danduri_Resume.pdf"


class ResumePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-0.5)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 0.15, "Varsha Danduri", align="C")


def section_title(pdf: ResumePDF, title: str) -> None:
    pdf.ln(0.08)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 0.18, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(200, 200, 200)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(0.06)


def entry_header(pdf: ResumePDF, title: str, date: str) -> None:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(0, 0.16, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(90, 90, 90)
    pdf.multi_cell(0, 0.15, date, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.02)


def bullet(pdf: ResumePDF, text: str) -> None:
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    x = pdf.l_margin
    pdf.set_x(x)
    pdf.cell(0.12, 0.15, "-")
    pdf.multi_cell(0, 0.15, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.02)


def body_line(pdf: ResumePDF, label: str, text: str) -> None:
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(30, 30, 30)
    pdf.write(0.15, label + " ")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 0.15, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.02)


def build() -> None:
    pdf = ResumePDF(unit="in", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=0.55)
    pdf.set_margins(0.65, 0.55, 0.65)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 0.25, "Varsha Danduri", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(80, 80, 80)
    contact = (
        "(302) 367-3997  |  varshadanduri@gmail.com  |  "
        "github.com/VarshaDanduri  |  linkedin.com/in/varsha-danduri-a7b22b375"
    )
    pdf.multi_cell(0, 0.14, contact, align="C")
    pdf.ln(0.1)

    section_title(pdf, "Education")
    entry_header(
        pdf,
        "University of Delaware, Honors College",
        "Newark, DE  |  May 2028",
    )
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        0.15,
        "B.S. + M.S. in Computer Science, 4+1 Accelerated Program  |  GPA 3.86",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    section_title(pdf, "Skills & Certifications")
    body_line(
        pdf,
        "Languages:",
        "Python, C, C++, Java, JavaScript / TypeScript, SQL",
    )
    body_line(
        pdf,
        "AI / ML:",
        "Model training and evaluation, NLP (tokenization, named-entity recognition), "
        "classifiers on medical and conversational data, LLM APIs (Anthropic, OpenAI), "
        "CrewAI multi-agent pipelines, GPU acceleration",
    )
    body_line(
        pdf,
        "Platforms & Tools:",
        "Flask, Node.js, PostgreSQL, Snowflake, GitHub Actions, VS Code, Conda, "
        "Android Studio, Xcode, Neovim",
    )
    body_line(
        pdf,
        "Certifications:",
        "PCEP Certified Python (2024), Udemy Python, Udemy ML / AI",
    )

    section_title(pdf, "Research Experience")
    entry_header(
        pdf,
        "Undergraduate Researcher, Healthy LAIfe Research Lab, University of Delaware",
        "June 2025 - Present",
    )
    bullet(
        pdf,
        "Built one of the first multimodal data pipelines on the widely used MIMIC-IV health "
        "database, integrating structured records, clinical text, medical images, and physiological "
        "signals into a single system for medical research. Open-sourced on GitHub with 300+ stars.",
    )
    bullet(
        pdf,
        "Trained models on the pipeline's output for medical research tasks and built a web "
        "interface that lets researchers define cohorts and pull data efficiently.",
    )
    bullet(
        pdf,
        "Co-authored a research paper currently under review; presented a scientific poster at UD "
        "Summer Scholars and was invited to present at the Naval Academy Science and Engineering "
        "Conference (November 2025).",
    )

    entry_header(
        pdf,
        "Chatbot Safety & Risk-Deferral Model",
        "Research  |  Python, Machine Learning, App Deployment",
    )
    bullet(
        pdf,
        "Built a model, deployed in an app, that reads user responses in chatbot conversations "
        "and flags signs of mental-health crisis in real time.",
    )
    bullet(
        pdf,
        "Designed a deferral layer: when risk is flagged, the chatbot steps back and the "
        "conversation is routed to safety resources and escalation instead of a generated reply, "
        "directly targeting a known failure mode of conversational AI.",
    )

    section_title(pdf, "Experience")
    entry_header(pdf, "Agentic Software Engineer, University of Delaware", "December 2025 - May 2026")
    bullet(
        pdf,
        "Designed and deployed a multi-step agentic workflow (Windmill) that runs the department's "
        "TA / RA recruiting pipeline end-to-end, plus a full-stack dashboard (React, Node.js, "
        "PostgreSQL) that staff use to manage every student worker.",
    )

    entry_header(pdf, "Software Engineer, University of Delaware IT", "February 2026 - Present")
    bullet(
        pdf,
        "Engineered a CI/CD pipeline (GitHub Actions, Jest) validating a jQuery migration tool "
        "used across the university's enterprise web applications.",
    )

    section_title(pdf, "Projects")
    entry_header(pdf, "NLP Python Package for Medical Notes", "C++, Python, GPU Acceleration")
    bullet(
        pdf,
        "Developed a Python package with a C++ core for processing medical notes: tokenization "
        "for training transformers and classifiers, GPU-accelerated text segmentation, and automatic "
        "disease named-entity recognition mapped to ICD codes.",
    )

    entry_header(
        pdf,
        "Kitin, Agentic Codebase Security Dashboard",
        "Startup, funded by University of Delaware  |  AI Agents, Cloudflare, React",
    )
    bullet(
        pdf,
        "Built an autonomous AI agent that does contextual code-logic analysis to catch "
        "vulnerabilities (e.g., SQL injection) that line-by-line tools miss, paired with a "
        "fine-tuned LoRA model and a git-automation engine with a full audit trail.",
    )

    entry_header(
        pdf,
        "Skin Disease Classification App",
        "Machine Learning, Node.js, Android (Edge)",
    )
    bullet(
        pdf,
        "Trained an image classification model on the DermNet dataset and deployed it in a web and "
        "Android app for early detection and awareness of skin conditions.",
    )

    section_title(pdf, "Awards & Recognition")
    bullet(
        pdf,
        "Best Modeling, UD DataQuest 2026: strongest predictive model in a university-wide data "
        "science competition.",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
