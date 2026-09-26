brus = 24.90
smørbrød = 45
banan = 8.50
totalsum = brus + smørbrød + banan
print("Totalsum", totalsum)
totalsum_med_mva = totalsum * 1.25
print("Totalsum med mva", totalsum_med_mva)
pris_per_person = totalsum / 4
print("Pris per person", pris_per_person)
prisforskjell = smørbrød - banan
print("Prisforskjell mellom smørbrød og banan", prisforskjell)
print(type(totalsum))
print(type(pris_per_person))
# --- Refleksjon ---
# Jeg fikk float som datatype.
# Siden brus og banan var desimaltall, så ble totalsummen også et desimaltall.
# Når jeg delte totalsummen på 4, ble datatypen float. 
# Fordelen er at hvis prisen hadde endret seg så hadde jeg bare trengt å endre på variabelen.
