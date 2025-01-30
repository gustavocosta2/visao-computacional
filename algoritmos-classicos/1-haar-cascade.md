# Algoritmo Haar Cascade.

O algoritmo Haar Cascade é uma técnica de *Machine Learning* que é empregada na detecção de qualquer coisa, isso dependerá do contexto ao qual ele será empregado. Por exemplo: a detecção de faces, detecção de pessoas, cachorros, objetos, etc.

## 1. Funcionamento

### 1.1. Coleta de Dados
Como todo algoritmo de ML, ele precisará de dados para ser treinado e testado. Para o Haar Cascade, há a criação de dois conjuntos:

- Conjunto 1: Fotos de faces (suponha que nosso contexto será realizar uma detecção facial), essas fotos serão consideradas as fotos **positivas**.
- Conjunto 2: Fotos não faciais, pode ser qualquer objeto desde que não seja uma face, são as chamadas fotos **negativas**.

### 1.2. Utilização do Algoritmo AdaBoost
Ele combina vários classificadores fracos - fraco = erra um pouco mais do que acerta - com o objetivo de criar um **classificador forte**.

- Cada classificador fraco tenta identificar se uma característica está presente ou não. Ex: olho, boca, sobrancelha, etc.
- Inicialmente, todos os classificadores fracos possuem o mesmo peso.
- Se o classificador acerta uma foto positiva então seu peso **aumenta**, se não, ele é **penalizado e seu peso diminui**.
- Assim, o AdaBoost combina esses classificadores de maior peso para criar um **classificador forte**.

Observação: cada classificador simples baseia-se em uma *Haar Feature* e, essas, vêm de um estudo sobre *Haar Wavelets** que procuram encontrar características que mais conseguem discernir um ponto-chave da face (boca, nariz, olhos, etc).

<div align=center>
  <img src="https://i.ibb.co/MkxLpHb0/Types-of-Haar-features.png" width=500px height=300px> 
</div>

<p align=center><i>img 1: Haar Features</i></p>

Cada Haar Feature será "deslizada" em subregiões da imagem para tentar encontrar **bordas** pela diferença de intensidade de pixels pretos pelos pixels brancos.

<p align=center><b>Pixels Pretos (255) - Pixels Brancos (0)</b></p>
<p align=center>|</p>
<p align=center>|</p>
<p align=center>V</p>
<p align=center>A cada resultado de cada Haar Feature aplicada na imagem, será colocado o resultado em uma <b>matriz de intensidade.</b></p>

### 1.3. Feature Selection
O AdaBoost seleciona os classificadores mais eficazes para criar uma **cascata de classificadores** para reduzir a complexidade computacional, isso significa que caso um dos classificadores negativos dê o resultado como False, não há porquê de continuar utilizando os
outros classificadores.

<div align=center>
  <img src="https://i.ibb.co/ynp97G8n/Cascade-classifier-illustration-2.jpg" width=500px height=300px> 
</div>

<p align=center><i>img 2: Haar Cascade</i></p>
