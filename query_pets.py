import sqlite3

def main():

    con = sqlite3.connect('Person.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Person")
        rows = cur.fetchall()

    value = 0
    while value != -1:
        value = input("Please enter the person id\n")
        if int(value) == -1 or int(value) < -1 or int(value) > len(rows):
            break

        print(f"{rows[int(value)-1][1]} {rows[int(value)-1][2]}, {rows[int(value)-1][3]} years old.")


if __name__ == '__main__':
    main()