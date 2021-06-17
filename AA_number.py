file = open('Exon1.txt', 'r')
f = open("Ex1_number.odt", "a+")
f.write("Ala Cys Asp Glu Phe Gly His Ile Lys Leu Met Asn Pro Asp Arg Ser Trp Val Thr Tyr"+ "\n")
for line in file:
	A = (line.count('A')) #Ala
    C = (line.count('C')) #Cys
    D = (line.count('D')) #Asp
    E = (line.count('E')) #Glu
    F = (line.count('F')) #Phe
    G = (line.count('G')) #Gly
    H = (line.count('H')) #His
    I = (line.count('I')) #Ile
    K = (line.count('K')) #Lys
    L = (line.count('L')) #Leu
    M = (line.count('M')) #Met
    N = (line.count('N')) #Asn
    P = (line.count('P')) #Pro
    Q = (line.count('Q')) #Asp
    R = (line.count('R')) #Arg
    S = (line.count('S')) #Ser
    T = (line.count('T')) #Trp
    V = (line.count('V')) #Val
    W = (line.count('W')) #Thr
    Y = (line.count('Y')) #Tyr
	f.write(str(A) + " " + str(C) + " " + str(D) + " " + str(E) + " " + str(F) + " " + str(G) + " " + str(H) + " " + str(I) + " " + str(K) + " " + str(L) + " " + str(M) + " " + str(N) + " " +str(P) + " " + str(Q) + " " + str(R) + " " + str(S) + " " + str(T) + " " + str(V) + " " + str(W) + " " + str(Y) + "\n")
file.close()
f.close() 