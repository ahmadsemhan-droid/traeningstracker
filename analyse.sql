

SELECT ovelser.navn, log.kg,log.reps, log.dato
FROM ovelser
JOIN log ON ovelser.id = log.ovelse_id;


select * 
from ovelser 
join log on ovelser.id = log.ovelse_id;


select ovelser.dag,ovelser.navn,log.kg
from ovelser 
join log on ovelser.id = log.ovelse_id;

-- Seneste test pr. øvelse
SELECT ovelse_id, MAX(dato)
FROM log
GROUP BY ovelse_id;

-- Nuværende PR
SELECT ovelser.navn, MAX(log.dato) AS seneste_test, log.kg
FROM log
JOIN ovelser ON ovelser.id = log.ovelse_id
GROUP BY log.ovelse_id;