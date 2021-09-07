class Score: 
    def __init__(self, match, miss, gap):
        self.gap = gap
        self.match = match
        self.miss = miss

def CreateMatriz(qnt_lines, qnt_columns, default_value):
    matriz = []
    for i in range(qnt_lines):
        line = []
        for j in range(qnt_columns):
            line.append(default_value)
        matriz.append(line)
    return matriz

def sigma(a, b, score):
    return score.match if a == b else score.miss

def AlignPD (a, b, score, gap_char="-"):
    m = a.__len__()
    n = b.__len__()
    M = CreateMatriz(n, m, 0)
    for i in range(0, n):
        M[i][0] = score.gap * i
    for j in range(0, m):
        M[0][j] = score.gap * j

    for i in range(1, n):
        for j in range(1, m):
            A = M[i - 1][j - 1] + sigma(a[j], b[i], score)
            B = M[i][j - 1] + score.gap
            C = M[i - 1][j] + score.gap 
            M[i][j] = max(A,B,C) 
    
    i = n-1
    j = m-1
    aSequence = ""
    bSequence = ""
    while True:
        if i == 0 and j == 0:            
            aSequence = a[j] + aSequence
            bSequence = b[i] + bSequence
            break

        if M[i-1][j-1] + sigma(a[j], b[i], score) == M[i][j]:
            aSequence = a[j] + aSequence
            bSequence = b[i] + bSequence
            i -= 1
            j -= 1
            continue

        if M[i-1][j] + score.gap == M[i][j]:
            aSequence = a[j] + aSequence
            bSequence = gap_char + bSequence
            i -= 1
            continue
        
        if M[i][j-1] + score.gap == M[i][j]:
            aSequence = gap_char + aSequence
            bSequence = b[i] + bSequence
            j -= 1
            continue
        break


    return (aSequence, bSequence, M[n-1][m-1])

seq1 = "TTACACCTAGC"
seq2 = "TAGCAATTTTTTCC"
print(AlignPD(seq1, seq2, Score(3, -2, -3)))

"""
Algoritmo AlignPD
Entrada: α, m, β, n 
Para todo i ∈ [0..n] faça M[i, 0] ← gap ∗ i 
Para todo j ∈ [1..m] faça M[0, j] ← gap ∗ j 


Para todo i ∈ [1..n] faça
    Para todo j ∈ [1..m] faça 
        A = M[i − 1, j − 1] + σ(α[j], β[i])
        B = M[i, j − 1] + gap
        C = M[i − 1, j] + gap 
        M[n,m] = máximo(A, B, C)
    FimPara
FimPara
Devolva M[n, m]"""