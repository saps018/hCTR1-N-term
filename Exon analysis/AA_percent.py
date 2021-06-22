file = open('Exon1.txt', 'r')
f = open("Ex1_percent.odt", "a+")
f.write("Ala Cys Asp Glu Phe Gly His Ile Lys Leu Met Asn Pro Asp Arg Ser Trp Val Thr Tyr"+ "\n")
for line in file:
	tot = len(line)-1
	A = (line.count('A'))*100/tot #Ala
    C = (line.count('C'))*100/tot #Cys
    D = (line.count('D'))*100/tot #Asp
    E = (line.count('E'))*100/tot #Glu
    F = (line.count('F'))*100/tot #Phe
    G = (line.count('G'))*100/tot #Gly
    H = (line.count('H'))*100/tot #His
    I = (line.count('I'))*100/tot #Ile
    K = (line.count('K'))*100/tot #Lys
    L = (line.count('L'))*100/tot #Leu
    M = (line.count('M'))*100/tot #Met
    N = (line.count('N'))*100/tot #Asn
    P = (line.count('P'))*100/tot #Pro
    Q = (line.count('Q'))*100/tot #Asp
    R = (line.count('R'))*100/tot #Arg
    S = (line.count('S'))*100/tot #Ser
    T = (line.count('T'))*100/tot #Trp
    V = (line.count('V'))*100/tot #Val
    W = (line.count('W'))*100/tot #Thr
    Y = (line.count('Y'))*100/tot #Tyr
	f.write(str(A) + " " + str(C) + " " + str(D) + " " + str(E) + " " + str(F) + " " + str(G) + " " + str(H) + " " + str(I) + " " + str(K) + " " + str(L) + " " + str(M) + " " + str(N) + " " +str(P) + " " + str(Q) + " " + str(R) + " " + str(S) + " " + str(T) + " " + str(V) + " " + str(W) + " " + str(Y) + "\n")
file.close()
f.close() 