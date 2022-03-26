-- INSERT INTO dojos (name)
-- VALUES ("Amsterdam"), ("Copenhagen"),("Online");

SET SQL_SAFE_UPDATES = 0;

INSERT INTO ninjas (first_name,last_name,age,dojos_id)
VALUES ("Adrien","Dion",22,10),("Anne","Jurack",21,10),("Ryan","Magley",23,10);

INSERT INTO ninjas (first_name,last_name,age,dojos_id)
VALUES ("Marisa","Goode",20,11),("Todd","Enders",24,11),("Sadie","Flick",25,11);

INSERT INTO ninjas (first_name,last_name,age,dojos_id)
VALUES ("Mr. Nibbles","Pancakes",33,12),("Benny Bob","McBob",31,12),("Mitch","Golden",32,12);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
WHERE dojos.id = 4;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);
    
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojos_id FROM ninjas ORDER BY dojos_id DESC LIMIT 1);