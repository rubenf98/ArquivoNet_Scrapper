# Scrapper: ArquivoNet

## _Inteligência Artificial para classificação de imagens com informação temporal_

O projeto ArquivoNet visa a criação de um sistema inteligente para classificação de imagens com perspectivas temporais, permitindo uma análise histórica das imagens armazenadas no Arquivo.pt. O projeto é inspirado em duas necessidades emergentes na área da inteligência artificial (IA). Primeiramente a criação de uma solução alimentada por informação temporal que proporciona uma visão única e adaptável da evolução de eventos e objetos ao longo do tempo. Esta perspetiva temporal dos objetos possibilita a implementação de soluções adaptáveis para problemas passados, presentes e futuros.

Em segundo lugar, há cada vez mais necessidade de um maior volume de dados que permitam métodos de IA mais generalizáveis. Os avanços tecnológicos atuais requerem cada vez mais informação que, apesar de pertencerem muitas vezes ao domínio público, carecem de protocolos de filtragem e processamento essenciais para o desenvolvimento destas tecnologias.

A recolha de imagens foi concebida pelo nosso algoritmo Scrapper, desenvolvido em python, que realiza a pesquisa e download de imagens preservadas no Arquivo.pt através da ImageSearch API v1.1. O algoritmo baseia-se na classe, subclasse e offset (index inicial) para gerar os argumentos de pesquisa utilizados na pesquisa da API. Posteriormente, o download das imagens é realizado utilizando o campo imgLinkToArchive de cada campo extraído da resposta JSON. Cada imagem foi identificada com o nome da respectiva classe, subclasse e o timestamp (imgTstamp) de forma a facilitar a sua identificação.

Expressamos a nossa gratidão ao Arquivo.pt por fornecer um recurso tão valioso, que foi essencial para o desenvolvimento bem-sucedido do ArquivoNet. Estamos ansiosos para continuar contribuindo para o avanço da compreensão da história digital.
