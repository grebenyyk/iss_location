import matplotlib.pyplot as plt
import requests
import cartopy.crs as ccrs


def get_iss_coords():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    coords = response.json()
    lat = float(coords['iss_position']['latitude'])
    lon = float(coords['iss_position']['longitude'])
    return lat, lon


def plot_coords(lat, lon):
    plt.clf()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()
    print(type(ax))
    plt.plot(lon, lat, color='red', linewidth=2, marker='o')
    plt.tight_layout()
    plt.show()


lat, lon = get_iss_coords()
plot_coords(lat, lon)
