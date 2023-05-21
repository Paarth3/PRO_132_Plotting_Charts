import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('star_with_gravity.csv')
mass = []
radius = []
gravity = []

df.drop(columns='Unnamed: 0', axis=0, inplace=True)
all_rows = df.values.tolist()

for row in all_rows:
    mass.append(row[2])
    radius.append(row[3])
    gravity.append(row[4])

for i in range(len(mass)-1, -1, -1):
    try:
        if str(mass[i]) == 'nan' or str(radius[i]) == 'nan' or str(gravity[i]) == 'nan':
            raise Exception("Error")
        mass[i] = float(mass[i])
        radius[i] = float(radius[i])
        gravity[i] = float(gravity[i])
    except:
        all_rows.pop(i)
        mass.pop(i)
        radius.pop(i)
        gravity.pop(i)

mass.sort()
radius.sort()
gravity.sort()

fig = plt.figure(figsize=(10,5))
plt.bar(mass, radius)

plt.xlabel("Mass")
plt.ylabel("Radius")
plt.title("Mass & Radius")
plt.show()

fig = plt.figure(figsize=(10,5))
plt.bar(mass, gravity)

plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.title("Mass & Gravity")
plt.show()