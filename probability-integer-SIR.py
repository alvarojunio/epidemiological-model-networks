import math

class graph:
    def __init__(self):
        s = input().split()
        self.n = int(s[0])
        self.m = int(s[1])
        s = input().split()
        self.alpha = []
        for i in range(len(s)):
            self.alpha.append(float(s[i]))
        s = input().split()
        self.bound_S = []
        self.S=[]
        for i in range(self.n):
            #self.bound_S.append(int(int(s[i]) * 0.05))
            #self.S.append(int(int(s[i]) * 0.05))
            self.bound_S.append(int(s[i]))
            self.S.append(int(s[i]))
        s = input().split()
        self.bound_I = []
        self.I = []
        for i in range(self.n):
            #self.bound_I.append(int(int(s[i]) * 0.05))
            #self.I.append(int(int(s[i]) * 0.05))
            self.bound_I.append(int(s[i]))
            self.I.append(int(s[i]))
        #s = input().split() => adicionar linha dos recuperados nos arquivos de entrada
        self.bound_R = []
        self.R = []
        for i in range(self.n):
            self.bound_R.append(0)
            self.R.append(0)
        self.adj = []
        for i in range(self.n):
            self.adj.append([])
        for i in range(self.m):
            s = input().split()
            u = int(s[0])
            v = int(s[1])
            mi = float(s[2])
            (self.adj[u]).append(v)
            (self.adj[v]).append(u)
            #TODO: armazenar mi!!!
    
    def __str__(self):
        s = "\nGraph printed:\n\n"
        s += "%23s" %("# vertices and # edges:")
        s += "%4d %4d\n" %(self.n, self.m)
        s+= "%23s" %("Isolation indices:")
        for i in range(self.n):
            s += "%4.2f " %self.alpha[i]
        s += "\n"
        s+= "%23s" %("Suscetibles:")
        for i in range(self.n):
            s += "%4d " %self.bound_S[i]
        s += "\n"
        s+= "%23s" %("Infected:")
        for i in range(self.n):
            s += "%4d " %self.bound_I[i]
        s += "\n"
        s+= "%23s" %("Recovered:")
        for i in range(self.n):
            s += "%4d " %self.bound_R[i]        
        s += "\n"
        s += "%23s" %("Edges and moviments:")
        s += "\n"
        for i in range(self.n):
            for j in range(len(self.adj[i])):
                s += "%27d %4d %c\n" %(i, self.adj[i][j], '?')
        return s
    
    def print_suscetible_infected(self, t):
        print("%3d" %t)
        for i in range(self.n):
            print("%2d %.2f %.2f" %(i, self.S[i], self.I[i]))
        
        print("*************************************")
        
    def print_suscetible_infected_recovered(self, t):
        print("%3d" %t)
        for i in range(self.n):
            print("%2d %.2f %.2f %.2f" %(i, self.bound_S[i], self.bound_I[i], self.bound_R[i]))
        
        print("*************************************")
        
    def print_suscetible_infected_recovered_vertex(self, t, i):
        print("%3d %.2f %.2f %.2f" %(t, self.bound_S[i], self.bound_I[i], self.bound_R[i]))
    
    def print_total_suscetible_infected(self, t):
        numS = 0
        numI = 0
        for i in range (self.n):
            numS += self.bound_S[i]
            numI += self.bound_I[i]
        
        print("%3d %7.2f %7.2f" %(t, numS, numI))
    
    def print_total_suscetible_infected_with_expected_value(self, t):
        numS = 0
        numI = 0
        numSEV = 0
        numIEV = 0
        for i in range (self.n):
            numS += self.bound_S[i]
            numI += self.bound_I[i]
            numSEV += self.S[i]
            numIEV += self.I[i]
        
        print("%3d %7.2f %7.2f %7.2f %7.2f" %(t, numS, numI, numSEV, numIEV))
    
    def print_total_suscetible_infected_recovered_with_expected_value(self, t):
        numS = 0
        numI = 0
        numR = 0
        numSEV = 0
        numIEV = 0
        numREV = 0
        for i in range (self.n):
            numS += self.bound_S[i]
            numI += self.bound_I[i]
            numR += self.bound_R[i]
            numSEV += self.S[i]
            numIEV += self.I[i]
            numREV += self.R[i]
        
        print("%3d %7d %7d %7d %7.2f %7.2f %7.2f" %(t, numS, numI, numR, numSEV, numIEV, numREV))
        
    def print_total_suscetible_infected_recovered(self, t):
        numS = 0
        numI = 0
        numR = 0
        for i in range (self.n):
            numS += self.bound_S[i]
            numI += self.bound_I[i]
            numR += self.bound_R[i]
        
        print("%3d %7.2d %7.2d %7.2d %7.2d" %(t, numS, numI, numR, numS + numI + numR))
            
def escolhe_2_de_n(n):
    return int(((n-1)*(n))/2)

def sum_n (N):
    soma = 0
    for i in range(len(N)):
        soma += N[i]
    return soma
   
def clear_lists(dot_S_t_i, dot_I_t_i, dot_R_t_i, ddot_S_t_i, ddot_I_t_i, ddot_R_t_i, math_dot_S_t_i, math_dot_I_t_i, math_dot_R_t_i, math_ddot_S_t_i, math_ddot_I_t_i, math_ddot_R_t_i, math_dddot_S_t_i, math_dddot_I_t_i, math_dddot_R_t_i, math_dot_N_t_i, math_ddot_N_t_i, math_dddot_N_t_i):
    dot_S_t_i.clear()
    dot_I_t_i.clear()
    dot_R_t_i.clear()
    ddot_S_t_i.clear()
    ddot_I_t_i.clear()
    ddot_R_t_i.clear()
        
    math_dot_S_t_i.clear()
    math_dot_I_t_i.clear()
    math_dot_R_t_i.clear()
    math_ddot_S_t_i.clear()
    math_ddot_I_t_i.clear()
    math_ddot_R_t_i.clear()
    math_dddot_S_t_i.clear()
    math_dddot_I_t_i.clear()
    math_dddot_R_t_i.clear()
    math_dot_N_t_i.clear()
    math_ddot_N_t_i.clear()
    math_dddot_N_t_i.clear()
    
def combination(n, k):
    fatn = math.factorial(n)
    fatk = math.factorial(k)
    fatnk = math.factorial(n-k)
    return fatn / (fatk * fatnk)
    
def binomial_distribution(n, p):
    q = 1 - p
    for k in range(n+1):
        print(k, combination(n, k) * math.pow(p,k) * math.pow(q,n-k))
        
def binomial_distribution(n, k, p):
    q = 1 - p
    return combination(n, k) * math.pow(p,k) * math.pow(q,n-k)

def module_sin_distribution(k):
    return math.fabs(math.sin(math.radians(k)))
    
def create_star_graph(n, alpha, S, I):
    m = n - 1
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(1, n):
        print(0, v, 1)
    
def create_complete_graph(n, alpha, S, I):
    m = (n * (n-1)) // 2
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(n):
        for w in range(v+1, n):
            print(v, w, 1)
        
def create_cycle_graph(n, alpha, S, I):
    m = n
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(n):
        print(v, (v + 1) % n, 1)
        
def create_path_graph(n, alpha, S, I):
    m = n - 1
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(n - 1):
        print(v, v + 1, 1)
        
def create_wheel_graph(n, alpha, S, I):
    m = 2*(n - 1)
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(1, n):
        print(0, v, 1)
    for v in range(1, n):
        print(v, (v + 1) % n, 1)
        
def create_binary_tree(n, alpha, S, I):
    m = n - 1
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(n//2):
        print(v, 2 * v + 1, 1)
        print(v, 2 * v + 2, 1)

#uma grade n1 x n2 (n1 = linhas, n2 = colunas)
def create_grid_graph(n1, n2, alpha, S, I):
    n = n1 * n2
    m = (n2 - 1) * n1 + (n1 - 1) * n2
    print(n, m)
    for i in range(n):
        print(alpha, end=" ")
    print()
    for i in range(n):
        print(S, end=" ")
    print()
    for i in range(n):
        print(I, end=" ")
    print()
    for v in range(n1):
        for u in range(n2 - 1):
            print(v * n2 + u, v * n2 + u + 1, 1)
    for v in range(n1 - 1):
        for u in range(n2):
            print(v * n2 + u, (v+1) * n2 + u, 1)
    
def main():
    
    #for k in range(100+1):
    #    print(k, binomial_distribution(100, k, 0.2))
    #return
    
    #for k in range(100+1):
    #    print(k, 0.7* module_sin_distribution(k*6))
    #return
    
    #create_star_graph(100, 1, 300, 0)
    #create_complete_graph(100, 1, 300, 0)
    #create_cycle_graph(100, 1, 300, 0)
    #create_path_graph(100, 1, 300, 0)
    #create_wheel_graph(100, 1, 300, 0)
    #create_binary_tree(127, 1, 300, 0)
    #create_grid_graph(10, 10, 1, 300, 0)
    #return
    
    G = graph()
    
    #fator de pessoas isoladas (suscetíveis ou infectadas) de um vértice qualquer que precisam sair
    lambda_dot_S = 0.4
    lambda_dot_I = 0.1
    lambda_dot_R = 0.6
    
    tfim = 200 #200 -> path graph
    epsilon = 0.145 # média de 1.45 pessoa recuperada em 10 dias 
    virulence = 0.455 # 45.5% de chance de um suscetível ser infectado em um encontro com um infectado
    
    dot_S_t_i = []
    dot_I_t_i = []
    dot_R_t_i = []
    ddot_S_t_i = []
    ddot_I_t_i = []
    ddot_R_t_i = []
    
    math_dot_S_t_i = []
    math_dot_I_t_i = []
    math_dot_R_t_i = []
    math_ddot_S_t_i = []
    math_ddot_I_t_i = []
    math_ddot_R_t_i = []
    math_dddot_S_t_i = []
    math_dddot_I_t_i = []
    math_dddot_R_t_i = []
    math_dot_N_t_i = []
    math_ddot_N_t_i = []
    math_dddot_N_t_i = []
    
    SP = 0
    RJ = 1
    ES = 2
    MG = 3
    PR = 4
    SC = 5
    RS = 6
    MS = 7
    MT = 8
    GO = 9
    DF = 10
    BA = 11
    SE = 12
    AL = 13
    PE = 14
    PB = 15
    RN = 16
    CE = 17
    PI = 18
    MA = 19
    TO = 20
    AP = 21
    PA = 22
    RR = 23
    AM = 24
    AC = 25
    RO = 26
    
    #G.print_suscetible_infected_recovered(0)
    #G.print_suscetible_infected_recovered_vertex(0, BA)
    G.print_total_suscetible_infected_recovered(0)
    #G.print_total_suscetible_infected_recovered_with_expected_value(0)
    
     
    for t in range(1, tfim + 1):
        
        clear_lists(dot_S_t_i, dot_I_t_i, dot_R_t_i, ddot_S_t_i, ddot_I_t_i, ddot_R_t_i, math_dot_S_t_i, math_dot_I_t_i, math_dot_R_t_i, math_ddot_S_t_i, math_ddot_I_t_i, math_ddot_R_t_i, math_dddot_S_t_i, math_dddot_I_t_i, math_dddot_R_t_i, math_dot_N_t_i, math_ddot_N_t_i, math_dddot_N_t_i)
        
        for i in range(G.n):
            #suscetíveis e infectados que aderiram isolamento social
            #sem isolamento social
            #dot_S_t_i.append(int((G.alpha[i] - 1) * G.bound_S[i]))
            #dot_I_t_i.append(int((G.alpha[i] - 1) * G.bound_I[i]))
            #dot_R_t_i.append(int((G.alpha[i] - 1) * G.bound_R[i]))
            #isolamento cíclico: um ciclo de 10 dias com pico de 70% de isolamento no 5 dia
            dot_S_t_i.append(int(G.alpha[i] * (.7 * module_sin_distribution(t*18)) * G.bound_S[i]))
            dot_I_t_i.append(int(G.alpha[i] * (.7 *  module_sin_distribution(t*18)) * G.bound_I[i]))
            dot_R_t_i.append(int(G.alpha[i] * (.7 *  module_sin_distribution(t*18)) * G.bound_R[i]))
            #isolamento constante (1 - x)%
            #dot_S_t_i.append(int((G.alpha[i] - .6) * G.bound_S[i]))
            #dot_I_t_i.append(int((G.alpha[i] - .6) * G.bound_I[i]))
            #dot_R_t_i.append(int((G.alpha[i] - .6) * G.bound_R[i]))
            #dot_S_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.45) * 10 * G.bound_S[i])))
            #dot_I_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.45) * 10 * G.bound_I[i])))
            #dot_R_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.45) * 10 * G.bound_R[i])))
            #dot_S_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.35) * 10 * G.bound_S[i])))
            #dot_I_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.35) * 10 * G.bound_I[i])))
            #dot_R_t_i.append(int(G.alpha[i] * binomial_distribution(tfim, t, 0.35) * 10 * G.bound_R[i])))
            #suscetíveis e infectados que NÃO aderiram isolamento social
            ddot_S_t_i.append(G.bound_S[i] - dot_S_t_i[i])
            ddot_I_t_i.append(G.bound_I[i] - dot_I_t_i[i])
            ddot_R_t_i.append(G.bound_R[i] - dot_R_t_i[i]) 
        
        for i in range(G.n):
            #a. parcela de pessoas suscetíveis de \dot{S}_i^t isoladas socialmente que circulam no vertice i
            math_dot_S_t_i.append(int(lambda_dot_S * dot_S_t_i[i]))
            #b. parcela de pessoas infectadas de \dot{I}_i^t isoladas socialmente que ciruculam no vértice i
            math_dot_I_t_i.append(int(lambda_dot_I * dot_I_t_i[i]))
            #g. parcela de pessoas recuperadas de \dot{I}_i^t isoladas socialmente que ciruculam no vértice i
            math_dot_R_t_i.append(int(lambda_dot_R * dot_R_t_i[i]))
            #c. parcela de pessoas suscetíveis de \ddot{S}_i^t NÃO isoladas socialmente que circulam no vértice i
            math_ddot_S_t_i.append(int(ddot_S_t_i[i] / (len(G.adj[i]) + 1)) + ddot_S_t_i[i] % (len(G.adj[i]) + 1))
            #d. parcela de pessoas infectadas de \ddot{I}_i^t NÃO isoladas socialmente que circulam no vértice i
            math_ddot_I_t_i.append(int(ddot_I_t_i[i] / (len(G.adj[i]) + 1)) + ddot_I_t_i[i] % (len(G.adj[i]) + 1))
            #h. parcela de pessoas recuperadas de \ddot{I}_i^t NÃO isoladas socialmente que circulam no vértice i
            math_ddot_R_t_i.append(int(ddot_R_t_i[i] / (len(G.adj[i]) + 1)) + ddot_R_t_i[i] % (len(G.adj[i]) + 1))
            #e. / f. / i. parcela de pessoas suscetíveis / infectadas / recuperadas de vértices vizinhos do vértice i NÃO isoladas socialmente e que circulam no vértice i
            sum_math_dddot_S_t_i = 0
            sum_math_dddot_I_t_i = 0
            sum_math_dddot_R_t_i = 0
            for j in G.adj[i]:             
                sum_math_dddot_S_t_i += int(ddot_S_t_i[j] / (len(G.adj[j]) + 1))
                sum_math_dddot_I_t_i += int(ddot_I_t_i[j] / (len(G.adj[j]) + 1))
                sum_math_dddot_R_t_i += int(ddot_R_t_i[j] / (len(G.adj[j]) + 1))
                
            math_dddot_S_t_i.append(sum_math_dddot_S_t_i)
            math_dddot_I_t_i.append(sum_math_dddot_I_t_i)
            math_dddot_R_t_i.append(sum_math_dddot_R_t_i)
            
            #total math_dots_N_t_i (S + I + R)
            math_dot_N_t_i.append(math_dot_S_t_i[i] + math_dot_I_t_i[i] + math_dot_R_t_i[i])
            math_ddot_N_t_i.append(math_ddot_S_t_i[i] + math_ddot_I_t_i[i] + math_ddot_R_t_i[i])
            math_dddot_N_t_i.append(math_dddot_S_t_i[i] + math_dddot_I_t_i[i] + math_dddot_R_t_i[i])
        
        for i in range(G.n):
            
            E_S_i_t = G.bound_S[i]
            E_I_i_t = G.bound_I[i]
            E_R_i_t = G.bound_R[i]
            
            #**************Probability*******************************
            P_dot_Y_pi_t = (math_dot_I_t_i[i] + math_ddot_I_t_i[i] + math_dddot_I_t_i[i])/(math_dot_N_t_i[i] + math_ddot_N_t_i[i] + math_dddot_N_t_i[i] - 1)
            
            P_ddot_Y_pii_t = P_dot_Y_pi_t
            
            sum_P_ddot_pij_t = 0
            for j in G.adj[i]: 
                sum_P_ddot_pij_t += (math_dot_I_t_i[j] + math_ddot_I_t_i[j] + math_dddot_I_t_i[j])/(math_dot_N_t_i[j] + math_ddot_N_t_i[j] + math_dddot_N_t_i[j] - 1)
            
                        
            #bounds over expedted values
            G.bound_I[i] = (E_I_i_t - int(math.ceil(epsilon * E_I_i_t))) + int(math.floor(virulence * (math_dot_S_t_i[i] * P_dot_Y_pi_t + (math_ddot_S_t_i[i] * P_ddot_Y_pii_t) + ((int((ddot_S_t_i[i] / (len(G.adj[i]) + 1)))) * sum_P_ddot_pij_t))))
            G.bound_S[i] = E_S_i_t - int(math.floor(virulence * (math_dot_S_t_i[i] * P_dot_Y_pi_t + (math_ddot_S_t_i[i] * P_ddot_Y_pii_t) + ((int((ddot_S_t_i[i] / (len(G.adj[i]) + 1)))) * sum_P_ddot_pij_t))))
            G.bound_R[i] = E_R_i_t + int(math.ceil(epsilon * E_I_i_t))
            
            #expected values
            G.I[i] = (E_I_i_t - epsilon * E_I_i_t) + (virulence * (math_dot_S_t_i[i] * P_dot_Y_pi_t + (math_ddot_S_t_i[i] * P_ddot_Y_pii_t) + ((math.floor(ddot_S_t_i[i] / (len(G.adj[i]) + 1))) * sum_P_ddot_pij_t)))
            G.S[i] = E_S_i_t - (virulence * (math_dot_S_t_i[i] * P_dot_Y_pi_t + (math_ddot_S_t_i[i] * P_ddot_Y_pii_t) + ((math.floor(ddot_S_t_i[i] / (len(G.adj[i]) + 1))) * sum_P_ddot_pij_t))) 
            G.R[i] = E_R_i_t + epsilon * E_I_i_t
            
                                    
        #G.print_suscetible_infected_recovered(t)
        #G.print_suscetible_infected_recovered_vertex(t, BA)
        G.print_total_suscetible_infected_recovered(t)
        #G.print_total_suscetible_infected_recovered_with_expected_value(t)
            

main()
