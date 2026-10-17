

SELECT ovelser.navn, log.kg,log.reps, log.dato
FROM ovelser
JOIN log ON ovelser.id = log.ovelse_id;
