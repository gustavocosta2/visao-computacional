# Rastreamento x Detecção: Qual a Diferença?


## 1. Detecção
A detecção facial é empregada em muitos contextos na área da visão computacional, seja em vigilância, saúde, comércio, etc. A **detecção** tem como **objetivo principal identificar a presença de um objeto ou evento em um único momento**
(imagem ou frame de um vídeo). 

- Funcionamento:
  -   Localiza e classifica objetos (ex: carro, pessoa, cachorro) em uma cena.
  -   Usa algoritmos como YOLO, Faster R-CNN ou outro modelo de deep learning para reconhecer padrões.
  -   Não considera informações temporais.

A saída de um algoritmo de detecção geralmente são coordenadas de bounding boxes, máscaras de segmentação ou a classificação de objetos.


## 2. Rastreamento
O objetivo do **rastreamento** é seguir um objeto **já detectado ao longo do tempo**, mantendo sua identidade em sequências (por ex, vídeos ou frames consecutivos). Em outras palavras, no rastreamento o objetivo é encontrar o objeto no quadro
atual considerando que ele foi rastreado corretamente nos quadros anteriores e para isso ele levará em consideração a posição anterior do objeto, a velocidade e a direção do movimento. Dessa forma, o algoritmo irá descrever uma possível rota
baseando-se em cálculos probabílisticos.

Uma das vantagens do rastreamento é que como baseiam-se em quadros anteriores eles são resistentes à **oclusões** durante vídeos.
