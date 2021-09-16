import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    i = 0
    Subtra_traco_ling = []
    
    while i < 6:
        sub  = abs(as_a[i] - as_b[i])
        Subtra_traco_ling.append(sub)
        i = i + 1
        Grau_de_simil = ((sum(Subtra_traco_ling)) / 6)

    return Grau_de_simil  
                          
    pass

def calcula_assinatura(texto):
    count_total_d_sentencas = len(separa_sentencas(texto))  
    lista_d_sentencas = separa_sentencas(texto) 
    
    lista_d_frases = []
    count_caract_p_sentenca = 0
    for sentenca in lista_d_sentencas:
        count_caract_p_sentenca = len(sentenca) + count_caract_p_sentenca
        lista_d_frases = separa_frases(sentenca) + lista_d_frases 
    count_total_frases = len(lista_d_frases) 

    lista_d_palavras = []
    count_caract_p_frase = 0
    for frase in lista_d_frases:
        count_caract_p_frase = len(frase) + count_caract_p_frase
        lista_d_palavras = separa_palavras(frase) + lista_d_palavras 
    count_total_palavras = len(lista_d_palavras)
        
    count_tamanho_d_palavras = 0
    for palavra in lista_d_palavras:
        count_tamanho_d_palavras = len(palavra) + count_tamanho_d_palavras

    count_palavras_unicas = n_palavras_unicas(lista_d_palavras)
    
    count_palavras_diferentes = n_palavras_diferentes(lista_d_palavras)

    s = count_total_d_sentencas
    f = count_total_frases
    p = count_total_palavras
    t = count_tamanho_d_palavras
    u = count_palavras_unicas
    d = count_palavras_diferentes
    cs = count_caract_p_sentenca
    cf = count_caract_p_frase
    
    return [(t/p), (d/p), (u/p), (cs/s), (f/s), (cf/f)] 

    pass

def avalia_textos(textos, ass_cp):
    lista_d_simil = []
    for texto in textos:
        lista_d_simil.append(calcula_assinatura(texto))       
        
    Grau_simil = 1000000
    i = 0
    texto_infectado = 0
    while i < len(lista_d_simil):
        funcao_compara = compara_assinatura(lista_d_simil[i], ass_cp)
        
        i = i + 1

        if funcao_compara < Grau_simil:
            Grau_simil = funcao_compara
            texto_infectado = i 

    return (texto_infectado)

    pass
'''a = avalia_textos(le_textos(), [4.79, 0.72, 0.56, 80.5, 2.5, 31.6])
#print (a)'''
