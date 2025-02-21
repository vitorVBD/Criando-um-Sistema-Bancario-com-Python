# Objetivo geral
Criar um sistema bancário com operações: sacar, depositar e visualizar extrato

# Contexto
Fomos contratados por um grande banco para desenvolver seu novo sistema. Esse banco deseja modernizar suas operações e por isso escolheu a linguagem Python. Para primeira versão do seu sistema devemos implementar apenas 3 operações: sacar, depositar e visualizar extrato

- Operação de depósito: Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

- Operação de saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

- Operação de extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

# Tarefa

Utilizando o contexto dos arquivos do projeto, crie um texto em markdown para documentar o projeto e colocar no readme.md, incluindo tanto o sistema quanto o prompt para a criação da documentação. Crie sessões como: Um resumo do projeto, desafios a serem cumpridos, estrutura e organização das pastas, tecnologias e ferramentas utilizadas, licença, desenvolvedor do projeto etc.

utilize o template de readme a seguir:

<p align="center">
<img src="./assets/images/icons/readme-icon.png" alt="Spider-Man Multiverse" width="150" /> <br /> <b>Spider-Man | Multiversos</b> <br /> <sub><sup><b>(LANDING-PAGE-SPIDERMAN)</b></sup></sub> <br /> </p> <p align="center"> Este projeto é uma landing page dedicada ao universo do Homem-Aranha, apresentando diferentes versões do herói interpretadas por Tobey Maguire, Andrew Garfield e Tom Holland. A página é construída com HTML, CSS e JavaScript, proporcionando uma experiência visual rica e interativa. <br /> </p>

## Estrutura do Projeto

### Páginas Principais

- index.html: Página inicial com um carrossel de cards destacando as diferentes versões do Homem-Aranha.
- spiderman1.html: Página dedicada ao primeiro filme de cada ator.
- spiderman2.html: Página dedicada ao segundo filme de cada ator.
- spiderman3.html: Página dedicada ao terceiro filme de cada ator.

### Estrutura de Pastas

````
landing-page-spiderman
├── assets
│   ├── css
│   │   └── home-page-styles.css
│   ├── images
│   │   ├── icons
│   │   │   └── spider.svg
│   │   ├── pic-sm-bg-01.jpg
│   │   ├── pic-sm-bg-02.jpg
│   │   ├── pic-sm-bg-03.jpg
│   │   └── spiderman-01.png
│   └── scripts
│       └── script.js
├── index.html
└── pages
    ├── andrew-garfield
    │   ├── spiderman1.html
    │   ├── spiderman2.html
    ├── tobey-maguire
    │   ├── spiderman1.html
    │   ├── spiderman2.html
    │   └── spiderman3.html
    └── tom-holland
        ├── spiderman1.html
        ├── spiderman2.html
        └── spiderman3.html
````

### Funcionalidades

- Carrossel de Cards: Apresenta os três atores que interpretaram o Homem-Aranha, com links para suas respectivas páginas.
- Vídeos de Trailer: Cada página de filme inclui um vídeo de trailer que é reproduzido automaticamente.
- Galeria de Imagens: Galeria de imagens para cada filme, com suporte a Fancybox para visualização em tela cheia.

### Tecnologias Utilizadas

- HTML5: Estrutura das páginas.
- CSS3: Estilização das páginas.
- JavaScript: Funcionalidades interativas, como o carrossel de cards.
- Fancybox: Biblioteca para visualização de imagens em tela cheia.

### Licença

Este software é licenciado sob os termos da MIT License.

⌨️ Desenvolvido por [Vitor Bittencourt](https://github.com/vitorVBD)