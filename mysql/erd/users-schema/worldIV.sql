
-- 1
SELECT countries.name as "name", languages.language as "language", languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

-- 2
SELECT countries.name, COUNT(cities.name) as cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY  countries.name 
ORDER BY cities DESC;

-- 3
SELECT name, population, country_id FROM cities
WHERE cities.population > 500000
AND cities.country_id = (Select id FROM countries WHERE countries.name = "Mexico")
ORDER BY population DESC;

-- 4
SELECT countries.name as name, languages.language as language, languages.percentage as percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- 5
SELECT name, countries.surface_area, population FROM countries
WHERE surface_area < 501
AND population > 100000
ORDER BY surface_area DESC;

-- 6
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE capital > 200
AND government_form = "Constitutional Monarchy"
AND life_expectancy > 75;

-- 7
SELECT countries.name as country_name, cities.name as city_name, cities.district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires"
AND cities.population > 500000;

-- 8
SELECT countries.region, COUNT(countries.name) as countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC;
