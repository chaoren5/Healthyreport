import mysql.connector

db = mysql.connector.connect(host="keep.black", user="root", passwd="Ys.104808", database="session")
cursor = db.cursor()


def addSession(sessionid, name):
    sql = "INSERT INTO sessionlist (sessionid, name) VALUES (%s, %s);"
    val = (sessionid, name)
    cursor.execute(sql, val)
    db.commit()
    return cursor.rowcount


def rmSession(sessionid):
    sql = "DELETE FROM sessionlist where sessionid = '{}';".format(sessionid)
    cursor.execute(sql)
    db.commit()
    return cursor.rowcount


def getSession():
    sql = "SELECT sessionid, name FROM sessionlist;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
