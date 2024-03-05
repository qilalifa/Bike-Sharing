import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
day_data = pd.read_csv("day.csv")
hour_data = pd.read_csv("hour.csv")

# Data cleaning
day_data.drop_duplicates(inplace=True)
day_data.fillna(method='ffill', inplace=True)

hour_data.drop_duplicates(inplace=True)
hour_data.fillna(method='ffill', inplace=True)

# Weather
day_data["weathersit"] = day_data["weathersit"].replace({
    1: "Sunny",
    2: "Rain",
    3: "Heavy Rain"})
day_data["year"] = pd.to_datetime(day_data["dteday"]).dt.year
bike_counts_by_weather = pd.pivot_table(day_data, values="cnt", index="year", columns="weathersit", aggfunc="sum", fill_value=0)

#2011
day_data_2011 = day_data[day_data["year"] == 2011]
bike_counts_by_weather_2011 = pd.pivot_table(day_data_2011, values="cnt", index="year", columns="weathersit", aggfunc="sum", fill_value=0)

#2012
day_data_2012 = day_data[day_data["year"] == 2012]
bike_counts_by_weather_2012 = pd.pivot_table(day_data_2012, values="cnt", index="year", columns="weathersit", aggfunc="sum", fill_value=0)

#Hour
hour_data["year"] = pd.to_datetime(hour_data["dteday"]).dt.year
pivot_hour = pd.pivot_table(hour_data, values="cnt", index="hr", columns="year", aggfunc="sum", fill_value=0)

#2011
hour_data_2011 = hour_data[hour_data["year"] == 2011]
pivot_hour_2011 = pd.pivot_table(hour_data_2011, values="cnt", index="hr", columns="year", aggfunc="sum", fill_value=0)

#2012
hour_data_2012 = hour_data[hour_data["year"] == 2012]
pivot_hour_2012 = pd.pivot_table(hour_data_2011, values="cnt", index="hr", columns="year", aggfunc="sum", fill_value=0)

# Streamlit app

st.set_page_config(page_title=" Bike Sharing!")


st.title("🚴🏻 Bike Sharing!")
st.write(
    "Welcome ✨ to Bike Sharing! Halaman Dashboard ini berisi grafik mengenai data peminjaman sepeda milik kami! "
    "Dan grafik ini akan membantu kalian lebih memahami tentang Bike Sharing itu sendiri ✨, Terutama jika kalian berkeinginan untuk meminjam sepeda!"
)

st.markdown("---")
with st.container():
    st.header("✨ Cuaca")
    st.write("Grafik dibawah ini menampilkan pengaruh cuaca 🌥️ terhadap jumlah peminjaman sepeda untuk setiap tahunnya! "
             "Simak grafik dibawah ini, dan coba analisis grafiknya ya 🤗 "
             "Oh ya, kalian lebih suka bersepeda di cuaca apa?? ")
    col1, col2 = st.columns([1, 1])
    with col1:
        option = st.selectbox("Grafik berdasarkan tahun : ", ["2011", "2012", "All"])

    # Process data based on selected option
    if option == "2011":
        ax = bike_counts_by_weather_2011.plot(kind="bar", figsize=(10, 6))
        plt.title("Jumlah peminjaman Sepeda berdasarkan cuaca Tahun 2011")
        plt.xlabel("Cuaca")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(rotation=0)
        plt.legend(title="Cuaca")
        plt.grid(axis="y")
        plt.show()
        for p in ax.patches:
            height = p.get_height()
            ax.annotate('{}'.format(height),
                        xy=(p.get_x() + p.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        st.pyplot(plt)

    elif option == "2012":
        ax = bike_counts_by_weather_2012.plot(kind="bar", figsize=(10, 6), width=0.8)
        plt.title("Jumlah Peminjaman Sepeda berdasarkan Cuaca Tahun 2012")
        plt.xlabel("Cuaca")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(rotation=0)
        plt.legend(title="Tahun")
        plt.grid(axis="y")
        for p in ax.patches:
            height = p.get_height()
            ax.annotate('{}'.format(height),
                        xy=(p.get_x() + p.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        st.pyplot(plt)

    elif option == "All":
        ax = bike_counts_by_weather.unstack().plot(kind="bar", figsize=(10, 6), width=0.8)
        plt.title("Jumlah Peminjaman Sepeda berdasarkan Cuaca")
        plt.xlabel("Cuaca")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(rotation=0)
        plt.legend(title="Tahun")
        plt.grid(axis="y")
        for p in ax.patches:
            height = p.get_height()
            ax.annotate('{}'.format(height),
                        xy=(p.get_x() + p.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        st.pyplot(plt)

    st.write("Nah, bagaimana kalian sudah simak grafik diatas?? apa kalian sudah menganalisisnya? ")

    st.markdown("---")

    st.header("🕣 Jam")
    st.write(
        "Selanjutnya, Grafik dibawah ini menampilkan busy hour!, pada pukul berapa sepeda 🚲 paling banyak dipinjam, waah ✨ "
        "Simak grafik dibawah ya, dan analisis apa perbedaannya! "
        "Oh ya, dan menurut kalian kapan waktu yang pas untuk bersepeda? "
    )

    col3, col4 = st.columns([1, 1])
    with col3:
        option_2 = st.selectbox("Pilih", ["2011", "2012", "All"])

    # Process data based on selected option
    if option_2 == "2011":
        pivot_hour_2011.plot(kind="line", figsize=(10, 6), marker='o')
        plt.title("Jumlah Peminjaman Sepeda berdasarkan Jam")
        plt.xlabel("Jam")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(range(24))
        plt.grid(True)
        plt.legend(title="Tahun")
        st.pyplot(plt)

    elif option_2 == "2012":
        pivot_hour_2012.plot(kind="line", figsize=(10, 6), marker='o')
        plt.title("Jumlah Peminjaman Sepeda berdasarkan Jam")
        plt.xlabel("Jam")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(range(24))
        plt.grid(True)
        plt.legend(title="Tahun")
        st.pyplot(plt)

    elif option_2 == "All":
        pivot_hour.plot(kind="line", figsize=(10, 6), marker='o')
        plt.title("Jumlah Peminjaman Sepeda berdasarkan Jam")
        plt.xlabel("Jam")
        plt.ylabel("Jumlah Peminjaman Sepeda")
        plt.xticks(range(24))
        plt.grid(True)
        plt.legend(title="Tahun")
        st.pyplot(plt)

    st.write("Wah kalian sudah berada di halaman akhir! ✨"
             "Bagimana apa menyenangkan menyimak grafiknya?? Semoga grafik diatas bisa menambah wawasan kalian ya 🤗")
