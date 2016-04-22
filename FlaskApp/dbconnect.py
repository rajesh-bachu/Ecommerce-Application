import MySQLdb

def connection():
    conn = MySQLdb.connect(host="pythonprogramming.ckdqzljpe2py.us-east-1.rds.amazonaws.com",
                           user = "root",
                           passwd = "password",
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn