BEGIN TRANSACTION;
CREATE TABLE artist(id INT, name TEXT, album TEXT, song_name TEXT, track_num INT, length INT);
INSERT INTO "artist" VALUES(1,'Taylor Swift','Fearless','Fearless',1,241);
INSERT INTO "artist" VALUES(2,'Taylor Swift','Fearless','Fifteen',2,272);
INSERT INTO "artist" VALUES(3,'Taylor Swift','Fearless','Love Story',3,213);
INSERT INTO "artist" VALUES(4,'Taylor Swift','Fearless','Hey Stephen',4,248);
INSERT INTO "artist" VALUES(5,'Taylor Swift','Fearless','White Horse',5,212);
INSERT INTO "artist" VALUES(6,'Lady Gaga','Chromatica','Chromatica I',1,60);
INSERT INTO "artist" VALUES(7,'Lady Gaga','Chromatica','Alice',2,154);
INSERT INTO "artist" VALUES(8,'Lady Gaga','Chromatica','Stupid Love',3,188);
INSERT INTO "artist" VALUES(9,'Lady Gaga','Chromatica','Rain on Me',4,181);
INSERT INTO "artist" VALUES(10,'Lady Gaga','Chromatica','Free Woman',5,187);
COMMIT;