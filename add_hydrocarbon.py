
import sqlite3


######################################################################################################
############################## CREATING THE HYDROCARBON TABLE ########################################
######################################################################################################


#create a database 
def create_table(db_name,table_name, sql): 
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name = ?", (table_name,))
        result = cursor.fetchall()
        cursor.execute("drop table if exists {0}".format(table_name))
        db.commit()
        keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
            
#sql statement to add data to the database
if __name__ == "__main__":
    db_name = "Theoretical_Method.db"
    sql = """create table Theoretical
             (HydrocarbonID integer,
             Hydrocarbon text,
             DeltaH_CH4 real,
             DeltaH_CO2 real,
             DeltaH_H2O real,
             Delta_O2 null,
             Reactant text,
             Product text,
             Intermediate text,
             Molar_mass real,
             number_Carbon integer,
             primary key(HydrocarbonID))"""   
    create_table(db_name,"Theoretical", sql)

#########################################################################################################
###############################  INSERT VALUES IN THE TABLE  ############################################
#########################################################################################################

# insert values into the database
def insert_data(values):
    with sqlite3.connect("Theoretical_Method.db") as db:
        cursor = db.cursor()
        sql = "insert into Theoretical (HydrocarbonID, Hydrocarbon, DeltaH_CH4, DeltaH_CO2, DeltaH_H2O, Delta_O2, Reactant, Product, Intermediate, Molar_mass, number_Carbon) values (?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()
if __name__ == "__main__":

    # assign a variable to each hydrocarbon
    hydrocarbon = (1, "methane",-74.9, -393.7, -571.0, 0, "CH4[g] + 2O2[g]", "CO2[g] +  2H2O[l]", " C[s] + 2H2[g]", 16.0, 1)
    hydrocarbon2 = (2, "ethane" ,-83.7, -787.4, -856.5, 0,"C2H6[g] + 3.5O2[g]", "2CO2[g] + 3H2O[l]", "2C[s] + 3H2[g]", 30.1, 2)
    hydrocarbon3 = (3, "propane",-104.6, -1181.1, -1142.0, 0,"C3H8[g] + 5O2[g]", "3CO2[g] + 4H2O[l]", "3C[s] + 4H2[g]", 44.1, 3)
    hydrocarbon4 = (4, "butane" ,-125.5,-1574.8, -1427.5, 0, "C4H10[g] + 6.5O2[g]", "4CO2[g] + 5H2O[l]","4C[s] + 5H2[g]", 58.1, 4)
    hydrocarbon5 = (5, "pentane",-146.9, -1968.5, -1713.0, 0, "C5H12[g] + 8O2[g]", "5CO2[g] + 6H2O[l]", "5C[s] + 6H2[g]", 72.2, 5)
    hydrocarbon6 = (6, "hexane", -167.4, -2362.2, -1998.5, 0, "C6H14[g] + 9.5O2[g]","6CO2[g] + 7H2O[l'", "6C[s] + 7H2[g]", 86.2, 6)
    hydrocarbon7 = (7, "heptane", -187.9, -2755.9, -2284.0,0,  "C7H16[g] + 11O2[g]", "7CO2[g] + 8H2O[l]", "7C[s] + 8H2[g]", 100.2, 7)
    hydrocarbon8 = (8, "octane", -208.4,-3149.6, -2569.5,0,  "C8H18[g] + 12.5O2[g]", "8CO2[g] + 9H2O[l]", "8C[s] + 9H2[g]", 114.2, 8)
    hydrocarbon9 = (9, "nonane",-229.3, -3543.3, -2855.0,0,  "C9H20[g] + 14O2[g]", "9CO2[g] + 10H2O[l]", "9C[s] + 10H2[g]", 128.3, 9)
    hydrocarbon10 = (10, "decane",-249.4,-3937.0, -3140.5,0,  "C10H22[g] + 15.5O2[g]", "10CO2[g] + 11H2O[l]", "10C[s] + 11H2[g]", 142.3, 10)
    hydrocarbon11 = (11, "undecane",-270.3, -4330.7,-3426.0, 0, "C11H24[g] + 17O2[g]", "11CO2[g] + 12H2O[l]", "11C[s] + 12H2[g]", 156.3, 11)
    hydrocarbon12 = (12, "dodecane",-290.9, -4724.4,-3711.5, 0, "C12H26[g] + 18.5O2[g]", "12CO2[g] + 13H2O[l]", "12C[s] + 13H2[g]", 170.3, 12)
    hydrocarbon13 = (13, "tridecane",-311.5,-5118.1, -3997.0, 0,  "C13H28[g] + 20O2[g]", "13CO2[g] + 14H2O[l]", "13C[s] + 14H2[g]", 184.4, 13)
    hydrocarbon14 = (14, "tetradecane",-332.1,-5511.8, -4282.5, 0, "C14H30[g] + 21.5O2[g]", "14CO2[g] + 15H2O[l]", "14C[s] + 15H2[g]", 198.4, 14)
    hydrocarbon15 = (15, "pentadecane",-354.8,-5905.5, -4568.0 ,0,  "C15H32[g] + 23O2[g]", "15CO2[g] + 16H2O[l]", "15C[s] + 16H2[g]", 212.4, 15)
    # *** insert new hydrocarbon here
    #hydrocarbon16 = (16, "test",-354.8,-5905.5, -4568.0 ,0,  "C15H32[g] + 23O2[g]", "15CO2[g] + 16H2O[l]", "15C[s] + 16H2[g]", 212.4, 15)    
    # insert hydrocarbon into database

    insert_data(hydrocarbon)
    insert_data(hydrocarbon2)
    insert_data(hydrocarbon3)
    insert_data(hydrocarbon4)
    insert_data(hydrocarbon5)
    insert_data(hydrocarbon6)
    insert_data(hydrocarbon7)
    insert_data(hydrocarbon8)
    insert_data(hydrocarbon9)
    insert_data(hydrocarbon10)
    insert_data(hydrocarbon11)
    insert_data(hydrocarbon12)
    insert_data(hydrocarbon13)
    insert_data(hydrocarbon14)
    insert_data(hydrocarbon15)
    # ***** insert_data(variable name i.e. hydrocarbon16) here 
    #insert_data(hydrocarbon16)
    

