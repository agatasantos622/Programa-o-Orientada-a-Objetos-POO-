# Programa-o-Orientada-a-Objetos-POO-
Projeto criado para a matéria de Algorithmic Thinking - Fevereiro 2026.

# 🏠 Orçamento Imobiliária R.M

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação em **Python**, utilizando conceitos de **Pensamento Algorítmico** e **Programação Orientada a Objetos (POO)**, com o objetivo de automatizar a geração de **orçamentos de aluguel** para uma imobiliária fictícia chamada **R.M**.

A aplicação permite calcular o valor do aluguel mensal de diferentes tipos de imóveis, aplicar acréscimos e descontos conforme regras de negócio e gerar automaticamente um arquivo de orçamento no formato **CSV**.

---

## 🎯 Objetivo

Automatizar o processo de geração de orçamentos imobiliários, facilitando o atendimento ao cliente e garantindo cálculos corretos, padronizados e organizados.

---

## 🏘️ Tipos de Imóveis Atendidos

* **Apartamento**
* **Casa**
* **Estúdio**

Cada tipo de imóvel possui regras específicas de cálculo, incluindo valores base, adicionais por quartos, garagem/vagas e descontos.

---

## ⚙️ Funcionalidades da Aplicação

* Seleção do tipo de imóvel
* Cálculo automático do aluguel mensal
* Aplicação de acréscimos por quartos e garagem/vagas
* Aplicação de desconto para apartamentos sem crianças
* Cálculo do contrato imobiliário (R$ 2.000,00 parcelado em até 5 vezes)
* Geração de arquivo **CSV** com 12 parcelas do orçamento mensal

---

## 🧠 Conceitos Utilizados

* Pensamento Algorítmico
* Programação Orientada a Objetos (POO)
* Herança e encapsulamento
* Estrutura condicional e repetição
* Manipulação de arquivos CSV

---

## 📁 Estrutura do Projeto

```
orcamento_imobiliario/
│
├── main.py              # Arquivo principal da aplicação
├── imovel.py            # Classes dos imóveis (POO)
├── contrato.py          # Classe responsável pelo contrato
├── gerador_csv.py       # Geração do arquivo CSV
├── parcelas_orcamento.csv  # Arquivo gerado automaticamente
└── README.md            # Documentação do projeto
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python **3.10 ou superior** (Python 3.12 compatível)
* Visual Studio Code ou outro editor Python

### Passos para execução

1. Abra a pasta do projeto no VS Code
2. Abra o terminal na pasta do projeto
3. Execute o comando:

```bash
python main.py
```

4. Siga as instruções exibidas no terminal

Ao final, um arquivo **parcelas_orcamento.csv** será gerado automaticamente.

---

## 📊 Exemplo de Saída

* Tipo do imóvel
* Valor do aluguel mensal
* Valor do contrato parcelado
* Arquivo CSV com 12 parcelas do orçamento

---

## 🚀 Possíveis Melhorias Futuras

* Geração de orçamentos individuais por cliente
* Histórico de orçamentos em um único arquivo
* Exportação para PDF
* Inclusão de interface gráfica ou aplicação web
* Validação avançada de entradas do usuário

---

## 🎥 Apresentação do Projeto

O projeto é acompanhado de um **vídeo pitch**, onde são apresentados:

* Objetivo da aplicação
* Estrutura do código
* Demonstração do funcionamento

---

## 👩‍💻 Autora

**Ágata Oliveira**
Projeto acadêmico – Algorithmic Thinking & Introduction to Object-Oriented Programming

---

📌 *Este projeto tem fins educacionais e demonstra a aplicação prática de conceitos fundamentais de programação.*
