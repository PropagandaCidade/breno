"""
BriefingBot - Criador de Briefings Profissionais
Transforma ideias em briefings estruturados para projetos
"""

import os
from datetime import datetime

BRIEFINGS_DIR = r"C:\Users\Usuario\.voice-hub\briefings"

def ensure_dir():
    if not os.path.exists(BRIEFINGS_DIR):
        os.makedirs(BRIEFINGS_DIR)

def make_briefing():
    print("=" * 60)
    print("BriefingBot - Criador de Briefings")
    print("=" * 60)
    print("\nVou fazer algumas perguntas para criar seu briefing.")
    print("Responda o que souber, pode deixar em branco também.\n")
    
    briefing = {}
    
    print("=== 1. INFORMAÇÕES BÁSICAS ===")
    briefing['nome_projeto'] = input("Nome do projeto: ").strip()
    briefing['cliente'] = input("Cliente/Titular: ").strip()
    briefing['data_criacao'] = datetime.now().strftime("%Y-%m-%d")
    briefing['prazo'] = input("Prazo (ex: 15/06/2026): ").strip()
    briefing['orcamento'] = input("Orçamento (ex: R$ 5.000): ").strip()
    
    print("\n=== 2. DESCRIÇÃO DO PROJETO ===")
    briefing['o_que_e'] = input("O que é o projeto? ").strip()
    briefing['objetivos'] = input("Objetivos principais: ").strip()
    briefing['problema'] = input("Problema a resolver: ").strip()
    briefing['publico_alvo'] = input("Público-alvo: ").strip()
    
    print("\n=== 3. REQUISITOS ===")
    briefing['funcionalidades'] = input("Funcionalidades necessárias: ").strip()
    briefing['restricoes'] = input("Restrições técnicas: ").strip()
    briefing['integracoes'] = input("Integrações necessárias: ").strip()
    
    print("\n=== 4. DESIGN ===")
    briefing['referencias'] = input("Referências visuais (sites, apps): ").strip()
    briefing['cores'] = input("Cores preferidas: ").strip()
    briefing['estilo'] = input("Estilo desejado (moderno, clássico, minimalista, etc): ").strip()
    briefing['concorrentes'] = input("Concorrentes/Reference: ").strip()
    
    print("\n=== 5. ENTREGÁVEIS ===")
    briefing['o_que_entregar'] = input("O que deve ser entregue: ").strip()
    briefing['formato'] = input("Formato final (site, app, design, etc): ").strip()
    briefing['prioridades'] = input("Prioridades: ").strip()
    
    print("\n=== 6. CRONOGRAMA ===")
    briefing['marcos'] = input("Marcos principais: ").strip()
    briefing['datas_importantes'] = input("Datas importantes: ").strip()
    
    print("\n=== 7. INFORMAÇÕES ADICIONAIS ===")
    briefing['equipe'] = input("Equipe responsável: ").strip()
    briefing['contato'] = input("Pessoa de contato: ").strip()
    briefing['obs'] = input("Observações extras: ").strip()
    
    return briefing

def generate_markdown(briefing):
    md = f"""# Briefing: {briefing['nome_projeto'] or 'Novo Projeto'}

**Data:** {briefing['data_criacao']}
**Cliente:** {briefing['cliente'] or 'Não informado'}
**Prazo:** {briefing['prazo'] or 'A definir'}
**Orçamento:** {briefing['orcamento'] or 'A definir'}

---

## 1. Descrição do Projeto

**O que é:** {briefing['o_que_e'] or 'Não informado'}

**Objetivos:** {briefing['objetivos'] or 'Não informado'}

**Problema a resolver:** {briefing['problema'] or 'Não informado'}

**Público-alvo:** {briefing['publico_alvo'] or 'Não informado'}

---

## 2. Requisitos

**Funcionalidades:** {briefing['funcionalidades'] or 'Não informado'}

**Restrições:** {briefing['restricoes'] or 'Não informado'}

**Integrações:** {briefing['integracoes'] or 'Não informado'}

---

## 3. Design

**Referências:** {briefing['referencias'] or 'Não informado'}

**Cores:** {briefing['cores'] or 'Não informado'}

**Estilo:** {briefing['estilo'] or 'Não informado'}

**Concorrentes/Reference:** {briefing['concorrentes'] or 'Não informado'}

---

## 4. Entregáveis

**O que entregar:** {briefing['o_que_entregar'] or 'Não informado'}

**Formato:** {briefing['formato'] or 'Não informado'}

**Prioridades:** {briefing['prioridades'] or 'Não informado'}

---

## 5. Cronograma

**Marcos:** {briefing['marcos'] or 'Não informado'}

**Datas importantes:** {briefing['datas_importantes'] or 'Não informado'}

---

## 6. Informações Adicionais

**Equipe:** {briefing['equipe'] or 'Não informado'}

**Contato:** {briefing['contato'] or 'Não informado'}

**Observações:** {briefing['obs'] or 'Não informado'}

---

*Briefing gerado por BriefingBot em {briefing['data_criacao']}*
"""
    return md

def main():
    ensure_dir()
    
    briefing = make_briefing()
    
    project_name = briefing['nome_projeto'].replace(' ', '-').lower() or 'novo-projeto'
    filename = f"{project_name}-{briefing['data_criacao']}.md"
    filepath = os.path.join(BRIEFINGS_DIR, filename)
    
    md = generate_markdown(briefing)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"\n{'=' * 60}")
    print(f"Briefing criado com sucesso!")
    print(f"Salvo em: {filepath}")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()