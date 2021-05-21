from docplex.mp.model import Model
import cplex

m = Model(name='Moveis')
x_1 = m.integer_var(name='x_1')
x_2 = m.integer_var(name='x_2')
m.add_constraint(2*x_1+x_2<=90)
m.add_constraint(x_1+4*x_2<=80)
m.add_constraint(3*x_1+2*x_2<=50)
m.add_constraint(x_1>=0)
m.add_constraint(x_2>=0)
m.maximize(100*x_1+120*x_2)
m.solve()
print(m.solution)
#m.export_as_lp("a.lp")
