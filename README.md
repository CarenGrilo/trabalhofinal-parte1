read.me

*APLICAÇÃO PARA INFORMAÇÕES SOBRE PREVISÃO DO TEMPO E ONDAS MARÍTIMAS*

Esse repositório é o trabalho de conclusão de curso de Python feito na CoderHouse (Turma 58865 - Profa Artemisia Weyl Potiguara).

Consiste num sistema que extrai dados de uma API que fornece previsão de tempo e também de ondas marítimas para várias cidades.
A API usada é a Brasil API e os dados são persistidos num banco de dados SQLite local.


*ESTRUTURA DO REPOSITÓRIO*
|-- __main__.py
|-- banco.db
|-- extract.py
|-- load.py
└── notification.py


*DESCRIÇÃO DOS ARQUIVOS*

__main__.py: código principal. Tem a função de orquestrar o repositório como um todo. Começa pelo carregamento dos dados e a verifica a base de dados.

banco.db: se trata de banco SQLite onde temos os dados das cidades, das previsões de tempo e das ondas.

extract.py: aqui está o repositório de todas as funções que vão extrair dados da API Brasil disponíveis no banco de dados.

load.py: esse arquivo gerencia a conexão com o banco de dados, cria tabelas, faz que os dados sejam persistidos no banco e verifica sua integridade.

notification.py: usa a biblioteca Plyer para notificar os eventuais erros ocorridos durante a extração dos dados.



*PRINCIPAIS FUNCIONALIDADES*

1. Extração de Dados
Utiliza a API Brasil API para obter informações sobre cidades, previsões de tempo e ondas marítimas.


2. Armazenamento em Banco de Dados
Cria tabelas no banco de dados SQLite (banco.db) para armazenar informações sobre cidades, previsões de tempo e ondas.
As tabelas são preenchidas com os dados extraídos da API, explicada no item 1..


3. Verificação do Banco de Dados
Verifica o número de registros nas tabelas de cidades, previsões de tempo e ondas no banco de dados.


4. Notificações de Erros
Caso ocorram erros na obtenção de dados de ondas para uma cidade específica, uma notificação é exibida utilizando a biblioteca Plyer.


*COMO USAR*

1. Pré-requisitos

- Python 3.x instalado.

2. Instalação das bibliotecas necessárias via pip:
- pip install requests plyer


3. Configuração
- Para clonar o repositório, execute os seguintes comandos:
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

- Para inicializar a aplicacão, execute o script principal para carregar o banco de dados:
python __main__.py


*CONTRIBUIÇÃO*
Todas as contribuições são bem-vindas! 
Fique muito a vontade. Qualquer opinião será fonte de aprendizado para todos nós!


*LICENÇA*
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
Fique muito a vontade. Qualquer contribuição será bem vinda e será fonte de aprendizado para todos nós!


Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
