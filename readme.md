<p align="center">
<img src="./assets/images/python-icon.png" alt="Sistema Bancário" width="150" /> <br />
<b>Sistema Bancário</b> <br />
<sub><sup><b>(BANCO-PYTHON)</b></sup></sub> <br />
</p>

<p align="center">
Este projeto implementa um sistema bancário simples utilizando a linguagem Python, permitindo ao usuário realizar depósitos, saques e consultar o extrato de sua conta bancária.
</p>

## Objetivo do Projeto
O projeto tem como objetivo criar um sistema bancário funcional com operações básicas de movimentação financeira, utilizando uma abordagem simples e eficiente para manipulação de valores em conta.

## Funcionalidades
- **Depósito**: Permite adicionar valores positivos à conta.
- **Saque**: Permite até 3 saques diários com limite de R$ 500,00 por saque.
- **Extrato**: Lista todos os depósitos e saques realizados, exibindo o saldo final.

## Requisitos do Sistema
- O sistema deve permitir apenas valores positivos nos depósitos.
- O limite de saques é de 3 por dia, com um teto de R$ 500,00 por saque.
- O saldo nunca pode ficar negativo.
- O extrato deve mostrar todas as movimentações realizadas.

## Estrutura do Projeto

```
BANCO-PYTHON
├── assets
│   ├── images
│   │   └── python-icon.png
├── prompts
│   ├── prompt_v1.md
├── src
│   ├── index.py
├── readme.md
```

## Tecnologias Utilizadas
- **Python**: Linguagem principal para implementação do sistema.
- **ChatGPT**: Utilizando Engenharia de Prompts para criar a documentação

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/banco-python.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd banco-python
   ```
3. Execute o arquivo principal:
   ```bash
   python src/index.py
   ```

## Licença
Este software está licenciado sob os termos da **MIT License**.

## Desenvolvedor
⌨️ Desenvolvido por [Vitor Bittencourt](https://github.com/vitorVBD)

