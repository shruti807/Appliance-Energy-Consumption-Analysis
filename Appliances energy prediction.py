import pandas as pd
import matplotlib.pyplot as plt


file_path = '/mnt/data/data_application_energy - data_application_energy.csv'
data = pd.read_csv(file_path)


data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y %H:%M')


plt.figure(figsize=(10,6))
plt.plot(data['date'], data['Appliances'], color='blue', label='Appliance Energy Consumption')
plt.xlabel('Date')
plt.ylabel('Energy Consumption (Wh)')
plt.title('Appliance Energy Consumption Over Time')
plt.grid(True)
plt.legend()
plt.show()

average_consumption = data['Appliances'].mean()
median_consumption = data['Appliances'].median()
total_consumption = data['Appliances'].sum()

print(f"Average Energy Consumption of Appliances: {average_consumption:.2f} Wh")
print(f"Median Energy Consumption of Appliances: {median_consumption:.2f} Wh")
print(f"Total Energy Consumption of Appliances: {total_consumption:.2f} Wh")
