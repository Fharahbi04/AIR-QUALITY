import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_changping = pd.read_csv("Dashboard/df_chang.csv")
df_guanyuan = pd.read_csv("Dashboard/df_guan.csv")
pollutants = df_changping.columns[5:11]
pollutants1 = df_guanyuan.columns[5:11]
# Asumsi dataframe memiliki kolom 'tahun'
min_year = min(df_changping['year'].min(), df_guanyuan['year'].min())
max_year = max(df_changping['year'].max(), df_guanyuan['year'].max())

# Slider untuk memilih rentang tahun
start_year, end_year = st.slider("Pilih Rentang Tahun", min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Filter data berdasarkan rentang tahun
df_changping_filtered = df_changping[(df_changping['year'] >= start_year) & (df_changping['year'] <= end_year)]
df_guanyuan_filtered = df_guanyuan[(df_guanyuan['year'] >= start_year) & (df_guanyuan['year'] <= end_year)]

with st.sidebar:
        st.image("Dashboard/air.png",width=300)
        st.title("AIR-QUALITY")
        
        option = st.selectbox(
        "DATA YANG INGIN DI TAMPILKAN",
        (
             "Pilihan",
        "Changping",
        "Guangyuan", 
    ),
        ) 

if option == "Pilihan":
    sns.set_style("whitegrid")
    
    # Menghitung rata-rata polutan per bulan di kedua stasiun
    monthly_avg_changping = df_changping_filtered.groupby("month")[pollutants].mean()
    monthly_avg_guanyuan = df_guanyuan_filtered.groupby("month")[pollutants1].mean()
    
    # Warna dan marker
    colors = sns.color_palette("tab10", len(pollutants))
    markers = ['o', 's', '^', 'D', 'v', 'P']
    
    # Membuat subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(monthly_avg_changping.index, monthly_avg_changping[pollutant],
                marker=markers[i], linestyle='-', color=colors[i], label=f"Changping - {pollutant}")
        ax.plot(monthly_avg_guanyuan.index, monthly_avg_guanyuan[pollutant],
                marker=markers[i], linestyle='dashed', color=colors[i], label=f"Guanyuan - {pollutant}")
        ax.set_title(f"{pollutant}", fontsize=12, fontweight='bold')
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Konsentrasi (µg/m³)")
        ax.set_xticks(range(1, 13))
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
    
    plt.suptitle("Rata-rata Polutan Udara Per Bulan", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(plt)
    
    # Perbandingan harian
    monthly_avg_changping = df_changping_filtered.groupby("day")[pollutants].mean()
    monthly_avg_guanyuan = df_guanyuan_filtered.groupby("day")[pollutants1].mean()
    
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    axes = axes.ravel()
    
    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(monthly_avg_changping.index, monthly_avg_changping[pollutant],
                marker=markers[i], linestyle='-', color=colors[i], label=f"Changping - {pollutant}")
        ax.plot(monthly_avg_guanyuan.index, monthly_avg_guanyuan[pollutant],
                marker=markers[i], linestyle='dashed', color=colors[i], label=f"Guanyuan - {pollutant}")
        ax.set_title(f"{pollutant}", fontsize=12, fontweight='bold')
        ax.set_xlabel("Hari")
        ax.set_ylabel("Konsentrasi (µg/m³)")
        ax.set_xticks(range(1, 32))
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()
    
    plt.suptitle("Rata-rata Polutan Udara Per Hari", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(plt)
     
elif option == "Changping":
    monthly_avg_changping = df_changping.groupby("month")[pollutants].mean()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_changping.index, y=monthly_avg_changping.mean(axis=1), marker="o",linewidth=2.5, color="blue")

    plt.title("Grafik Polutan di Changping",fontsize=13,fontweight="bold")
    plt.xlabel("Bulan",fontsize=13,fontweight="bold")
    plt.ylabel("Rata-rata",fontsize=13,fontweight="bold")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(plt)

    monthly_avg_changping = df_changping.groupby("day")[pollutants].mean()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_changping.index, y=monthly_avg_changping.mean(axis=1), marker="o",linewidth=2.5, color="blue")

    plt.title("Grafik Polutan di Changping",fontsize=13,fontweight="bold")
    plt.xlabel("Hari",fontsize=13,fontweight="bold")
    plt.ylabel("Rata-rata",fontsize=13,fontweight="bold")
    plt.xticks(range(1, 32))
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(plt)

elif option == "Guangyuan":
    monthly_avg_guanyuan = df_guanyuan.groupby("month")[pollutants1].mean()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_guanyuan.index, y=monthly_avg_guanyuan.mean(axis=1), marker="o",linewidth=2.5, color="blue")

    plt.title("Grafik Polutan di Guanyuan",fontsize=13,fontweight="bold")
    plt.xlabel("Bulan",fontsize=13,fontweight="bold")
    plt.ylabel("Rata-rata",fontsize=13,fontweight="bold")
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(plt)

    monthly_avg_guanyuan = df_guanyuan.groupby("day")[pollutants1].mean()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=monthly_avg_guanyuan.index, y=monthly_avg_guanyuan.mean(axis=1), marker="o",linewidth=2.5, color="blue")

    plt.title("Grafik Polutan di Guanyuan",fontsize=13,fontweight="bold")
    plt.xlabel("Hari",fontsize=13,fontweight="bold")
    plt.ylabel("Rata-rata",fontsize=13,fontweight="bold")
    plt.xticks(range(1, 32))
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(plt)



     # Menggunakan gaya seaborn agar lebih rapi
    sns.set_style("whitegrid")

    # Menghitung rata-rata polutan per bulan di kedua stasiun
    monthly_avg_changping = df_changping.groupby("month")[pollutants].mean()
    monthly_avg_guanyuan = df_guanyuan.groupby("month")[pollutants1].mean()

    # Warna dan marker untuk setiap polutan
    colors = sns.color_palette("tab10", len(pollutants))
    markers = ['o', 's', '^', 'D', 'v', 'P']

    # Membuat subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(monthly_avg_changping.index, monthly_avg_changping[pollutant],
                marker=markers[i], linestyle='-', color=colors[i], label=f"Changping - {pollutant}")
        ax.plot(monthly_avg_guanyuan.index, monthly_avg_guanyuan[pollutant],
                marker=markers[i], linestyle='dashed', color=colors[i], label=f"Guanyuan - {pollutant}")
        ax.set_title(f"{pollutant}", fontsize=12, fontweight='bold')
        ax.set_xlabel("Bulan")
        ax.set_ylabel("Konsentrasi (µg/m³)")
        ax.set_xticks(range(1, 13))
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()

    # Konfigurasi layout
    plt.suptitle("Rata-rata Polutan Udara Per Bulan", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(plt)


    sns.set_style("whitegrid")

    # Menghitung rata-rata polutan per bulan di kedua stasiun
    monthly_avg_changping = df_changping.groupby("day")[pollutants].mean()
    monthly_avg_guanyuan = df_guanyuan.groupby("day")[pollutants1].mean()

    # Warna dan marker untuk setiap polutan
    colors = sns.color_palette("tab10", len(pollutants))
    markers = ['o', 's', '^', 'D', 'v', 'P']

    # Membuat subplots
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    axes = axes.ravel()

    for i, pollutant in enumerate(pollutants):
        ax = axes[i]
        ax.plot(monthly_avg_changping.index, monthly_avg_changping[pollutant],
                marker=markers[i], linestyle='-', color=colors[i], label=f"Changping - {pollutant}")
        ax.plot(monthly_avg_guanyuan.index, monthly_avg_guanyuan[pollutant],
                marker=markers[i], linestyle='dashed', color=colors[i], label=f"Guanyuan - {pollutant}")
        ax.set_title(f"{pollutant}", fontsize=12, fontweight='bold')
        ax.set_xlabel("Hari")
        ax.set_ylabel("Konsentrasi (µg/m³)")
        ax.set_xticks(range(1, 32))
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend()

    # Konfigurasi layout
    plt.suptitle("Rata-rata Polutan Udara Per Hari", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(plt)



