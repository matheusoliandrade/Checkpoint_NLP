def ler_arquivo_e_criar_lista(caminho_arquivo):
    lista = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())  
    return lista

def pre_processamento(texto):
    separacao = texto.find("-")

    avaliacao = texto[:separacao]
    resto = texto[separacao + 1:]

    pontuacao = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

    stopwords = ler_arquivo_e_criar_lista("stopwords.txt")

    textof = ""

    for caractere in resto:
        if caractere not in pontuacao:
            textof += caractere

        textof = textof.lower()

        palavras = textof.split()

        palavras_filtradas = []

        for palavra in palavras:
            if palavra not in stopwords:
                palavras_filtradas.append(palavra)

        frase = palavras_filtradas

    return avaliacao, frase

pos = 0
neg = 0

t1 = input("Qual a sua opinião em relação a este produto?: ")
t2 = input("Quantas estrelas você daria para este produto (1 a 5): ")
texto = f"{t2} - {t1}"

avaliacao, frase = pre_processamento(texto)

palavras_positivas = ler_arquivo_e_criar_lista("Palavras_Positivas.txt")

palavras_negativas = ler_arquivo_e_criar_lista("Palavras_Negativas.txt")

for palavra in frase:
    if palavra in palavras_positivas:
       pos += 1
    elif palavra in palavras_negativas:
        neg += 1

if avaliacao == 1:
    neg += 2
elif avaliacao == 2:
    neg += 1
elif avaliacao == 3:
    if pos > neg:
        pos = pos - 2
    else:
        neg = neg - 2
elif avaliacao == 4:
    pos += 1
elif avaliacao == 5:
    pos += 2

if pos > neg:
    print("O sentimento deste texto é Positivo")
elif neg > pos:
    print("O sentimento deste texto é Negativo")
elif neg == pos:
    print("O sentimento deste texto é Neutro")








