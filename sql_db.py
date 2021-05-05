import sqlite3 as sql


def insert(dict):
    """
    INSERT METHODE for table tbl_carnet_address
    :param  a dictionnairy with all the relevant data
    """
    conn_db = sql.connect("db_carnet_address")
    cr = conn_db.cursor()
    cr.execute("INSERT INTO tbl_carnet_address VALUES(:nom, :prenom, :adress, :telephone)", dict)
    conn_db.commit()
    conn_db.close()


def delete(l_name, f_name):
    conn_db = sql.connect("db_carnet_address")
    cr = conn_db.cursor()
    cr.execute(f"DELETE FROM tbl_carnet_address WHERE nom = '{l_name}' and prenom = '{f_name}'")
    conn_db.commit()
    conn_db.close()


def update_entry(l_name, f_name, nom, prenom, n_add, n_phone):
    conn_db = sql.connect("db_carnet_address")
    cr = conn_db.cursor()
    cr.execute(f"""UPDATE tbl_carnet_address 
                SET nom = '{nom}', prenom = '{prenom}', adress = '{n_add}', telephone = '{n_phone}'
                WHERE nom = '{l_name}' and prenom = '{f_name}'
                """)
    conn_db.commit()
    conn_db.close()


def select(l_name, f_name):
    conn_db = sql.connect("db_carnet_address")
    cr = conn_db.cursor()
    cr.execute(f"SELECT adress, telephone FROM tbl_carnet_address WHERE nom ='{l_name}' and prenom = '{f_name}' ")
    record = cr.fetchone()
    conn_db.commit()
    conn_db.close()
    return record


def select_all():
    conn_db = sql.connect("db_carnet_address")
    cr = conn_db.cursor()
    cr.execute("SELECT * FROM tbl_carnet_address ORDER BY nom, prenom")
    record = cr.fetchall()
    conn_db.commit()
    conn_db.close()
    return record
