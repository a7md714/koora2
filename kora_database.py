import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('kora.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS match
                (id INTEGER PRIMARY KEY,
                teams TEXT,
                score_team_a TEXT,
                score_team_b TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS vid_match
                (id INTEGER PRIMARY KEY,
                last_vid TEXT)
                ''')


def addData(teams, scoreA, scoreB):
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Insert data into the table
    cursor.execute(
        "INSERT INTO match (teams,score_team_a,score_team_b) VALUES ( ?,?,?)",
        (teams, scoreA, scoreB))
    conn.commit()  # Commit the transaction



def getData(teams_name):
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM match WHERE teams=?", (teams_name, ))
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return row


def getAllData():
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM match ")
    row = cursor.fetchall()
    for r in row:
        print(r)
    cursor.close()
    conn.close()


def updateData(new_score_a, new_score_b, team_name):
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Update data in the table
    cursor.execute(
        "UPDATE match SET score_team_a = ?, score_team_b = ? WHERE teams = ?",
        (new_score_a, new_score_b, team_name))
    print('############UPDATE TEAM ############')
    conn.commit()  # Commit the transaction
    cursor.close()
    conn.close()


def delete():
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Delete all rows from each table
    for table in tables:
        cursor.execute("DELETE FROM " + table[0])

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


def addVidNum(vid_num):
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Insert data into the table
    cursor.execute(
        f"INSERT INTO vid_match (last_vid) VALUES ({vid_num})"
        )
    conn.commit()  # Commit the transaction
    conn.close()

def getVidData():
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vid_match ")
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return row
#print(getVidData()[1])
def updateVidData(new_vid_num):
    conn = sqlite3.connect('kora.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Update data in the table
    cursor.execute(
        f"UPDATE vid_match SET last_vid ={new_vid_num}"
        )
    print('############UPDATE video ############')
    conn.commit()  # Commit the transaction
    cursor.close()
    conn.close()

