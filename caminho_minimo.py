from docplex.mp.model import Model
import cplex

m = Model(name='CaminhoMinimo')
x_12 = m.binary_var(name='x_12')
x_13 = m.binary_var(name='x_13')
x_23 = m.binary_var(name='x_23')
x_24 = m.binary_var(name='x_24')
x_34 = m.binary_var(name='x_34')

m.add_constraint(x_12+x_13==1)
m.add_constraint(x_12-x_24-x_23==0)
m.add_constraint(x_13+x_23-x_34==0)
m.add_constraint(x_24+x_34==1)

m.minimize(10*x_12+28*x_13+15*x_23+35*x_24+13*x_34)
m.print_information()
m.solve()
print(m.solution)
