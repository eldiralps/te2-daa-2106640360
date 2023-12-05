import random

def generate_random_dataset(n):
    weights = [random.randint(1, 100) for _ in range(n)]
    values = [random.randint(1, 100) for _ in range(n)]
    W = int(0.1 * sum(weights))
    return weights, values, W

def save_to_txt(data, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, data)))

# Generate datasets untuk n = 100
dataset_n_100 = generate_random_dataset(100)
save_to_txt(dataset_n_100[0], '100_weights.txt')
save_to_txt(dataset_n_100[1], '100_values.txt')
save_to_txt([dataset_n_100[2]], 'W_100.txt')  # Menyimpan W ke dalam file terpisah

# Generate datasets untuk n = 1000
dataset_n_1000 = generate_random_dataset(1000)
save_to_txt(dataset_n_1000[0], '1000_weights.txt')
save_to_txt(dataset_n_1000[1], '1000_values.txt')
save_to_txt([dataset_n_1000[2]], 'W_1000.txt')

# Generate datasets untuk n = 10000
dataset_n_10000 = generate_random_dataset(10000)
save_to_txt(dataset_n_10000[0], '10000_weights.txt')
save_to_txt(dataset_n_10000[1], '10000_values.txt')
save_to_txt([dataset_n_10000[2]], 'W_10000.txt')

