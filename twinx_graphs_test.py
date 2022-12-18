year_list = who_data['year'].unique().tolist()
country_list = who_data['country'].unique().tolist()

for i in range(len(country_list)):
    country = country_list[i]
    data = who_data[who_data["country"] == country]
    #print(data)
    plt.subplot(2,3,(i+1))
    fig, ax1 = plt.subplots()
    ax1.plot(year_list, data['gdp_billions_usd'], marker='o', color='red')
    plt.ylabel("GDP (Billions of US Dollars)", color='red')
    plt.xticks(rotation=30)
    ax1.set_xticks(year_list)
    ax2 = ax1.twinx()
    ax2.plot(year_list, data['life_expectancy'], marker='o', color='green')
    plt.ylabel("Life Expectancy (Years)", color='green')
    fig.tight_layout()
    plt.title(country)
    plt.show()
    plt.clf()