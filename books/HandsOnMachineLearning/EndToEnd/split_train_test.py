import numpy as np 
def split_train_test(data, test_ratio):
    count = len(data)
    shuffled_indices = np.random.permutation(count)
    test_set_size = int(test_ratio * count)

    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    return data.iloc[train_indices], data.iloc[test_indices]