from docplex.mp.model import Model
import cplex

m = Model(name='ApFin')

variaveis = dict()

for i in range(1,7):
    variaveis[i] = m.continuous_var(name='x_{0}'.format(i))

for i in range(1,7):
    m.add_constraint(variaveis[i]<=187500)

m.add_constraint(variaveis[1]+variaveis[6]>=375000)
m.add_constraint(variaveis[2]+variaveis[3]+variaveis[5]<=262500)

for i in range(1,7):
    m.add_constraint(variaveis[i]>=0)
    
m.maximize(0.0865*variaveis[1]+0.0950*variaveis[2]+0.1*variaveis[3]
           +0.0875*variaveis[4]+0.0925*variaveis[5]+0.09*variaveis[6])

m.solve()
print(m.solution)
