# ~ Compatible with both python 2.7 & python 3
# ~ Make sure pandas is installed using: pip install --user pandas; pip3 install --user pandas;
from __future__ import print_function
import numpy as np
import sqlite3
from astropy.io import ascii
import pandas
import os

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
sql_statement = "SELECT  GRB_name_Fermi, ra, decl, T0, T90, redshift, fluence from Summary WHERE GRB_name_Fermi IN (?)"
for i in range(0, obj_numbers):
	# ~ print (grb_input_list[i])
	Summary_table = pandas.read_sql(sql_statement, db, params=(grb_input_list[i],))
	Summary_table_2 = Summary_table
	merged_Summary_table = Summary_table.merge(Summary_table_2, how='inner')
	print(Summary_table, "\n")
# ~ Summary_table.set_index('Conc', inplace=True)
# ~ print(merged_Summary_table, "\n")

# ~ Print the first entry in the Swift table
# ~ print("First entry in Swift table:")
# ~ keys = Swift_table.keys()
# ~ First_entry = Swift_table.values[0]
# ~ for key, value in zip(keys, First_entry):
    # ~ print("{:>12}:  {:<25}".format(key, value))

# ~ Get numpy arrays containing the right ascension, declination, mjd, ...
# ~ of the entries in the Summary table
# ~ Summary_table = pandas.read_sql_query("SELECT * from Summary", db)
# ~ keys = Summary_table.keys()
# ~ print("\n\nKeys in the 'Summary' table:", list(keys))
# ~ RA  = np.array(Summary_table.ra)   # right ascension
# ~ DEC = np.array(Summary_table.decl) # declination
# ~ MJD = np.array(Summary_table.mjd)  # modified julian date
# ~ print(" RA:", RA)
# ~ print(" DEC:", DEC)
# ~ print(" MJD:", MJD)
