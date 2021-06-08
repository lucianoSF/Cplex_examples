from docplex.mp.model import Model
import cplex

m = Model(name='Alocacao_de_motoristas')

i_j = {"1":"9", "5":"13", "9":"17", "13":"21", "17":"1", "21":"5"}

var_x = dict()

for item in i_j:
	var_x[item + i_j[item]] = m.integer_var(name='x_{0}_{1}'.format(item,i_j[item]))

m.add_constraint(var_x["215"] + var_x["19"]>=15)
m.add_constraint(var_x["19"] + var_x["513"]>=30)
m.add_constraint(var_x["513"] + var_x["917"]>=26)
m.add_constraint(var_x["917"] + var_x["1321"]>=32)
m.add_constraint(var_x["1321"] + var_x["171"]>=30)
m.add_constraint(var_x["171"] + var_x["215"]>=19)

for item in i_j:
	m.add_constraint(var_x[item + i_j[item]]>=0)
    
m.minimize(var_x["19"] + var_x["513"] + var_x["917"] + var_x["1321"] + var_x["171"] + var_x["215"])
m.solve()
print(m.solution)
#m.export_as_lp("a.lp")
