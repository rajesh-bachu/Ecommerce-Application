import MySQLdb

def connection():
    conn = MySQLdb.connect(host="rdsdb",
                           user = "user",
                           passwd = "password",
                           db = "Dbname")
    c = conn.cursor()

    return c, conn
