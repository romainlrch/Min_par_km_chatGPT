min_per_km = int(input("Entrez le nombre de minutes par kilomètre : "))
sec_per_km = int(input("Entrez le nombre de secondes par kilomètre : "))

# Convertir les minutes et secondes par kilomètre en heures par kilomètre
hours_per_km = (min_per_km * 60 + sec_per_km) / 3600

# Convertir les heures par kilomètre en kilomètres par heure
km_per_hour = 1 / hours_per_km

# Afficher la vitesse en kilomètres par heure
print("La vitesse est de :", km_per_hour, "km/h")
