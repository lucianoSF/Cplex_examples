from docplex.mp.model import Model
import cplex
m = Model(name='Transporte')

x_csp = m.integer_var(name='x_csp')
x_crj = m.integer_var(name='x_crj')
x_cv = m.integer_var(name='x_cv')
x_bhsp = m.integer_var(name='x_bhsp')
x_bhrj = m.integer_var(name='x_bhrj')
x_bhv = m.integer_var(name='x_bhv')


m.add_constraint(x_csp+x_bhsp==20)
m.add_constraint(x_crj+x_bhrj==25)
m.add_constraint(x_cv+x_bhv==25)
m.add_constraint(x_csp+x_crj+x_cv<=32)
m.add_constraint(x_bhsp+x_bhrj+x_bhv<=40)

m.add_constraint(x_csp >= 0)
m.add_constraint(x_crj >= 0)
m.add_constraint(x_cv >= 0)
m.add_constraint(x_bhsp >= 0)
m.add_constraint(x_bhrj >= 0)
m.add_constraint(x_bhv >= 0)

m.minimize(9*x_csp+16*x_crj+25*x_cv+27*x_bhsp+22*x_bhrj+21*x_bhv)
m.solve()
print(m.solution)
#m.export_as_lp("a.lp")
