Programação Orientada a Objetos (POO)

Projeto criado para a disciplina Algorithmic Thinking & Introduction to Object-Oriented Programming – Fevereiro/2026.

🎬 Vídeo de Apresentação
A apresentação completa do projeto, contendo a explicação do objetivo, estrutura do código, execução via terminal, interface gráfica com Streamlit e geração do arquivo CSV, está disponível no link abaixo:

🔗 https://www.linkedin.com/posts/%C3%A1gata-santos-628b8935a_python-poo-aprendizado-activity-7426455816016412672-nz3M?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFmE7EABUKiP6kx_EaoHd56PscMBNW3hYIY

🏠 Orçamento Imobiliária R.M
📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação em Python, utilizando conceitos de Pensamento Algorítmico e Programação Orientada a Objetos (POO), com o objetivo de automatizar a geração de orçamentos de aluguel para uma imobiliária fictícia chamada R.M.

A aplicação foi desenvolvida em duas versões:

Modo terminal (CLI), com interação via linha de comando

Interface gráfica web, desenvolvida com Streamlit, permitindo uma experiência visual e interativa

Ambas as versões utilizam a mesma lógica de negócio, garantindo reutilização de código e separação de responsabilidades.

🎯 Objetivo

Automatizar o processo de geração de orçamentos imobiliários, facilitando o atendimento ao cliente e garantindo cálculos corretos, padronizados e organizados, tanto em ambiente de terminal quanto por meio de uma interface gráfica.

🏘️ Tipos de Imóveis Atendidos

Apartamento

Casa

Estúdio

Cada tipo de imóvel possui regras específicas de cálculo, incluindo valores base, adicionais por quartos, garagem/vagas e descontos.

⚙️ Funcionalidades da Aplicação

Seleção do tipo de imóvel

Cálculo automático do aluguel mensal

Aplicação de acréscimos por quartos e garagem/vagas

Aplicação de desconto para apartamentos sem crianças

Cálculo do contrato imobiliário (R$ 2.000,00 parcelado em até 5 vezes)

Geração automática de arquivo CSV com 12 parcelas do orçamento

Interface gráfica interativa para geração de orçamentos

🧠 Conceitos Utilizados

Pensamento Algorítmico

Programação Orientada a Objetos (POO)

Herança e encapsulamento

Estruturas condicionais e de repetição

Manipulação de arquivos CSV

Separação entre lógica de negócio e interface gráfica

📁 Estrutura do Projeto
orcamento_imobiliario/
│
├── main.py                 # Execução via terminal
├── streamlit_app.py        # Interface gráfica com Streamlit
├── imovel.py               # Classes dos imóveis (POO)
├── contrato.py             # Classe responsável pelo contrato
├── gerador_csv.py          # Geração do arquivo CSV
├── parcelas_orcamento.csv  # Arquivo gerado automaticamente
└── README.md               # Documentação do projeto

▶️ Como Executar o Projeto
Pré-requisitos

Python 3.10 ou superior (Python 3.12 compatível)

Visual Studio Code ou outro editor Python

Streamlit (para a interface gráfica)

🔹 Execução via Terminal (modo tradicional)

Abra a pasta do projeto no VS Code

Abra o terminal na pasta do projeto

Execute o comando:

python main.py


Siga as instruções exibidas no terminal

Ao final, um arquivo parcelas_orcamento.csv será gerado automaticamente.

🔹 Execução com Interface Gráfica (Streamlit)

A aplicação também pode ser executada por meio de uma interface gráfica web, desenvolvida com Streamlit, permitindo maior usabilidade e interação visual.

Passos:

Instale o Streamlit (caso ainda não tenha):

pip install streamlit


Execute a aplicação gráfica:

streamlit run streamlit_app.py


O navegador será aberto automaticamente com link temporário:

http://localhost:8501

ou no link já disponibilizado em web:

https://orcamentosimobiliarios.streamlit.app/


Na interface gráfica, o usuário pode:

Selecionar o tipo de imóvel

Informar quartos, garagem, vagas e presença de crianças

Definir o parcelamento do contrato

Visualizar o orçamento calculado diretamente na tela

Gerar o arquivo CSV do orçamento

🖥️ Interface Gráfica (Streamlit)

A interface gráfica foi desenvolvida como uma evolução do sistema, mantendo toda a lógica de negócio separada da camada visual.

Características da interface:

Campos dinâmicos conforme o tipo de imóvel selecionado

Uso de componentes visuais como selectbox, checkbox, radio, slider e botões

Exibição clara e organizada dos valores calculados

Reutilização das classes e regras definidas no código principal

Essa abordagem demonstra boas práticas de desenvolvimento, como reutilização de código, manutenção facilitada e escalabilidade da aplicação.

📊 Exemplo de Saída

Tipo do imóvel

Valor do aluguel mensal

Valor do contrato parcelado

Arquivo CSV com 12 parcelas do orçamento

🚀 Possíveis Melhorias Futuras

Geração de orçamentos individuais por cliente

Histórico de orçamentos em um único arquivo

Exportação para PDF

Hospedagem da interface gráfica em nuvem

Validação avançada de entradas do usuário

🎥 Apresentação do Projeto

O projeto é acompanhado de um vídeo pitch, onde são apresentados:

Objetivo da aplicação

Estrutura do código

Demonstração do funcionamento no terminal e na interface gráfica

👩‍💻 Autora

Ágata Oliveira
Projeto acadêmico – Algorithmic Thinking & Introduction to Object-Oriented Programming

📌 Este projeto tem fins educacionais e demonstra a aplicação prática de conceitos fundamentais de programação e Programação Orientada a Objetos.
