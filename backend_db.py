import sqlite3

def connect():
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS servers (id INTEGER PRIMARY KEY, url text, connection text, port integer, priority integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS outputs (id INTEGER PRIMARY KEY, location text)")
    conn.commit()
    conn.close()

def insert(url, connection, port, priority):
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO servers VALUES (NULL,?, ?, ?,?)",(url, connection, port, priority))
    conn.commit()
    conn.close()

def view_locations():
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM outputs")
    rows=cur.fetchall()
    conn.close()
    return(rows)

def insert_location(location):
    conn=sqlite3.connect("servers.db")
    print(location)
    cur=conn.cursor()
    cur.execute("INSERT INTO outputs VALUES (NULL, ?)", ((location,)))
    conn.commit()
    conn.close()

def delete_location(id):
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM outputs WHERE id={}".format(id))
    conn.commit()
    conn.close()

def view_servers():
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM servers")
    rows=cur.fetchall()
    conn.close()
    return(rows)

def search(url="", connection="", port="", priority=""):
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM servers where url=? OR connection=? OR port=? OR priority=?",(url, connection, port, priority))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM servers WHERE id={}".format(id))
    conn.commit()
    conn.close()

def update(id, url, connection, port, priority):
    conn=sqlite3.connect("servers.db")
    cur=conn.cursor()
    cur.execute("UPDATE servers SET url=?, connection=?, port=?, priority=? WHERE id=?",(url, connection, port, priority, id))
    conn.commit()
    conn.close()