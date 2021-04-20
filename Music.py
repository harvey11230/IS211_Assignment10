import sqlite3 as lite

def main():

    artists = (
        (1, 'Taylor Swift', 'Fearless', 'Fearless', 1, 241),
        (2, 'Taylor Swift', 'Fearless', 'Fifteen', 2, 272),
        (3, 'Taylor Swift', 'Fearless', 'Love Story', 3, 213),
        (4, 'Taylor Swift', 'Fearless', 'Hey Stephen', 4, 248),
        (5, 'Taylor Swift', 'Fearless', 'White Horse', 5, 212),
        (6, 'Lady Gaga', 'Chromatica', 'Chromatica I', 1, 60),
        (7, 'Lady Gaga', 'Chromatica', 'Alice', 2, 154),
        (8, 'Lady Gaga', 'Chromatica', 'Stupid Love', 3, 188),
        (9, 'Lady Gaga', 'Chromatica', 'Rain on Me', 4, 181),
        (10, 'Lady Gaga', 'Chromatica', 'Free Woman', 5, 187)
    )

    con = lite.connect(':memory:')

    with con:

        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS music")
        cur.execute("CREATE TABLE artist(id INT, name TEXT, album TEXT, song_name TEXT, track_num INT, length INT)")
        cur.executemany("INSERT INTO artist VALUES(?, ?, ?, ?, ?, ?)", artists)

        data = '\n'.join(con.iterdump())

        writeData(data)

def writeData(data):

    f = open('music.sql', 'w')

    with f:
        f.write(data)

if __name__ == '__main__':
    main()