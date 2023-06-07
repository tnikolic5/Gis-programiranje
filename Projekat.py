import geopandas as gpd

# Učitavanje shapefailova
granica_path = r'C:\Users\Tijana\Desktop\Programiranje\Ispit\Jagodina.shp'
granica = gpd.read_file(granica_path)

shapefile_path = r'C:\Users\Tijana\Desktop\Programiranje\Ispit\Turisticke lokacije.shp'
turisticki_objekti = gpd.read_file(shapefile_path)

# Uvoženje biblioteke za prikazivanje mapa
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

# Prikazivanje turističkih objekata na teritoriji Grada Jagodina
granica.plot(ax=ax, color='lightgray', edgecolor='black')

turisticki_objekti.plot(ax=ax, marker='o', color='red', markersize=40)

plt.title('Mapa turističkih objekata na teritoriji Grada Jagodina')
ax.legend(['Turisticke lokacije', 'Granica Jagodine' ])
plt.show()

# Prikazivanje naziva turističkih objekata
turisticki_objekti.plot(column='Naziv', legend=True)
plt.title('Mapa turističkih objekata na teritoriji Grada Jagodina')
plt.show()
