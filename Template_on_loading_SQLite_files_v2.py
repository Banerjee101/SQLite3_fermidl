# ~ Compatible with both python 2.7 & python 3
# ~ Make sure pandas is installed using: pip install --user pandas; pip3 install --user pandas;
from __future__ import print_function,division
import numpy as np
import sqlite3, pandas, os, sys
from astropy.io import ascii

# ~ Download the SQLite file from the GRBweb 2 webpage
os.system("wget -N https://icecube.wisc.edu/~grbweb_public/GRBweb2.sqlite")

# ~ Load the database with the sqlite3 module
db = sqlite3.connect('GRBweb2.sqlite')
# ~ cur = db.cursor()
# ~ cur.execute

# ~ Print the names of all the tables
table_names = pandas.read_sql_query("SELECT * from sqlite_sequence", db)
print("Table names:\n", table_names, "\n\n")

# ~ From the list of table names we use select and print the tables that have the aforementioned grb names
grb_input_list = np.loadtxt("OBJ_FermiName_list", usecols=0, dtype = 'string')
# ~ print(grb_input_list)
obj_numbers = len(grb_input_list)
print("Summary table:\n")
sql_statement = "SELECT  GRB_name,GRB_name_Fermi, ra, decl, redshift from Summary WHERE redshift BETWEEN 0 AND 200"
Summary_table = pandas.read_sql(sql_statement, db)
Summary_table_2 = Summary_table
merged_Summary_table = Summary_table.merge(Summary_table_2, how='inner')
np.set_printoptions(threshold=sys.maxsize)
np.savetxt('redshift_op.txt', Summary_table, fmt='%s')
