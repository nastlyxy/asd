import pandas as pd
import matplotlib.pyplot as plt

# Читаем нашу таблицу
df = pd.read_csv('benchmark_results.csv')
algorithms = df['Algorithm'].unique()

# Рисуем график для каждого алгоритма
for algo in algorithms:
    plt.figure()
    algo_data = df[df['Algorithm'] == algo]
    
    # Рисуем линии для каждого типа массива (случайный, возрастающий и т.д.)
    for input_type in algo_data['InputType'].unique():
        subset = algo_data[algo_data['InputType'] == input_type]
        # Сортируем данные по размеру массива, чтобы линия шла ровно
        subset = subset.sort_values(by='InputSize')
        plt.plot(subset['InputSize'], subset['Time'], label=input_type, marker='o')
    
    plt.title(algo)
    plt.xlabel('Rozmiar tablicy (n)')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    # Сохраняем картинку
    plt.savefig(f'{algo}.png')
    plt.close()
    print(f"{algo}.png is ready")