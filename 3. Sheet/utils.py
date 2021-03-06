from typing import Tuple

import numpy as np


def train_test_idxs(L: int, test_ratio: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns indices that can be used as train and test data.

    Args:
        L (int): The size of the dataset
        test_ratio (float): The ratio [0-1] of indices that should be put in the test
        set

    Returns:
        Tuple[np.ndarray, np.ndarray]: The training and testset indices
    """
    rng = np.random.RandomState(0)
    idxs = rng.rand(L).argsort()
    te_len = int(L * test_ratio)

    te_idx = idxs[:te_len]
    tr_idx = idxs[te_len:]

    return tr_idx, te_idx
