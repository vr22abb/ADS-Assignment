import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
SEASONS = ["win", "spr", "sum", "aut"]
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
          "oct","nov", "dec"]
SEASONS_LABELS = ["Winter", "Spring", "Summer", "Autumn"]
MONTHS_LABELS = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November",
                 "December"]
# Functions
# select_years functions is to get the specified year data for processing
def select_years(rfdata, start_year, end_year):
    return rfdata[(rfdata['year'] >= start_year) &
                  (rfdata['year'] <= end_year)]

# Line Plot
def plot_line_chart(selected_year, start_year, end_year, save_plot_img):
    plt.figure(figsize=(12, 6))
    
    season_labels = {"win": "Winter", "spr": "Spring", "sum": "Summer",
                     "aut": "Autumn"}
    
    x = selected_year["year"]
    
    #Iterating seasons over year
    for season in SEASONS:
        y = selected_year[season]
        plt.plot(x, y, label=season_labels[season], marker='o')
    
    # Labelling the plot
    plt.xlabel('Year')
    plt.ylabel('Accumulated Rainfall in MM')
    plt.title(f'UK Rainfall Data ({start_year} - {end_year})')
    plt.xticks(x)
    plt.legend()
    plt.savefig(save_plot_img)

# Pie chart
def plot_pie_chart(selected_year, start_year, end_year, save_plot_img):
    
    total_rainfall = [selected_year[season].sum() for season in SEASONS]
    
    plt.figure(figsize=(7, 7))
    plt.pie(total_rainfall, labels=SEASONS_LABELS,
            autopct='%1.1f%%', startangle=140)
    plt.title(f'UK Seasonal Rainfall Data ({start_year} - {end_year})')
    plt.savefig(save_plot_img)

# Bar chart
def plot_bar_chart(selected_year, save_plot_img):
    years = selected_year['year']
    total_rainfall = selected_year['ann']
    
    max_rainfall_year = years[total_rainfall.idxmax()]
    min_rainfall_year = years[total_rainfall.idxmin()]
    
    plt.figure(figsize=(12, 6))
    
    bars = plt.bar(years, total_rainfall, color='blue')
    
    plt.bar([max_rainfall_year, min_rainfall_year],
            [total_rainfall.max(), total_rainfall.min()],
            color=['red', 'green'], label=['Max Rainfall', 'Min Rainfall'])
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{yval:.2f}',
                 ha='center', va='center', rotation=90, color='white')

    # Labelling the plot
    plt.xlabel('Year')
    plt.ylabel('Rainfall in (MM)')
    plt.title('UK Total Annual Rainfall Data') 
    plt.legend() 
    plt.xticks(years, rotation=90)
    plt.savefig(save_plot_img)

# Main code
# Reading the data
rfdata = pd.read_csv("/Users/diya/Documents/Rainfall Data - UK.csv")
rfdata = rfdata.dropna()

sns.set_style("whitegrid")

# Preparing the data
start_year = 2000
end_year = 2023

selected_year = select_years(rfdata, start_year, end_year)

# Function invoking
plot_line_chart(selected_year, start_year, end_year, "plot_line_chart.png")
plot_pie_chart(selected_year, start_year, end_year, "pie_chart.png")
plot_bar_chart(selected_year, "bar_chart.png")

#Display the plot
plt.show()
