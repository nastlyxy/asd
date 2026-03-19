import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_results.csv')
algorithms = df['Algorithm'].unique()

for algo in algorithms:
    plt.figure()
    algo_data = df[df['Algorithm'] == algo]
    
    for input_type in algo_data['InputType'].unique():
        subset = algo_data[algo_data['InputType'] == input_type]
        subset = subset.sort_values(by='InputSize')
        plt.plot(subset['InputSize'], subset['Time'], label=input_type, marker='o')
    
    plt.title(algo)
    plt.xlabel('Rozmiar tablicy (n)')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f'{algo}.png')
    plt.close()
    print(f"{algo}.png is ready")