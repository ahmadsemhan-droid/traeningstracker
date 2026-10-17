

SELECT ovelser.navn, log.kg,log.reps, log.dato
FROM ovelser
JOIN log ON ovelser.id = log.ovelse_id;


select * 
from ovelser 
join log on ovelser.id = log.ovelse_id;


select ovelser.dag,ovelser.navn,log.kg
from ovelser 
join log on ovelser.id = log.ovelse_id;