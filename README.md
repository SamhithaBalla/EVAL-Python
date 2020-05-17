# EVAL-Python
Automated tool for Bloom's taxonomy to aid faculty in designing question papers

Requirements:

Qt designer, SQLite3, ReportLab

1. create .ui files using PyQt designer and convert .ui to .py files using the command line utility as follows: (Open command prompt as administrator and set the path to the directory where the .ui files are saved)
     i) pyuic5 atbt.ui -o atbt.py
     ii) pyuic5 levels.ui -o levels.py
     iii) pyuic5 kywrds.ui -o kywrds.py
     iv) pyuic5 eval.ui -o eval.py
     v) pyuic5 genrep.ui -o genrep.py
2. Now develop python scripts atbt1.py, levels1.py, kywrds1.py, eval2.py, genrep1.py
3. Open SQLite and run the following commands
     i) .open atbt1


     ii) CREATE TABLE levels
(
lid varchar(3) NOT NULL,
ldesc varchar(25) NOT NULL
);


     iii) CREATE TABLE kywrds
(
lid varchar(3) NOT NULL,
kywrd varchar(25) NOT NULL, per number(10) NOT NULL
);


     iv) .save atbt1
4. Open command prompt as administrator and set the path to the directory where all project files are stored and run the command :
     python atbt1.py
