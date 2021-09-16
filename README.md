# Similaridade entre textos - Caso COH-PIAH
> status: Finalizado


Este programa foi desenvolvido para a entrega do projeto final de conclusão do curso: Introdução à Ciência da Computação com Python. 
Link: https://www.coursera.org/learn/ciencia-computacao-python-conceitos


Dependência interna:
- re.


Objetivos:
- Familiarizar-se com o módulo "re" utilizando, sobretudo, a função "split";
- Utilizar e interagir com código escrito por terceiros.


Observações:
- As funções pré-existentes são:
    - le_assinatura,
    - le_textos,
    - separa_sentencas,
    - separa_frases,
    - separa_palavras,
    - n_palavras_unicas,
    - n_palavras_diferentes.

- Explicação do Problema:
    - Detecção de autoria.
      Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.
      
    - Traços linguísticos.
     Estatísticas para detectar a doença:
    Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    Complexidade de sentença: Média simples do número de frases por sentença.
    Tamanho médio de frase: Média simples do número de caracteres por frase.
