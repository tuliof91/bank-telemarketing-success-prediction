from collections import Counter
import math
import pandas as pd
import pytest


import bank_deposit_classifier.sample as sample

# def test_oversample_minority_class(data):
#     data_ = sample.oversample_minority_class(data, 'y', 0.5)
#     assert isinstance(data_, pd.DataFrame)

@pytest.mark.parametrize("p", [(0.5), (0.75), (0.9)])
def test_oversample_minority_class(data, p):
    outcome = 'y'
    outcome_counts = Counter(data[outcome])
    minority_class, _ = outcome_counts.most_common()[-1]

    data_ = sample.oversample_minority_class(data, outcome, p)
    n_minority = data_.loc[data_[outcome] == minority_class].shape[0]
    n_total = data_.shape[0]
    p_minority = n_minority/n_total

    assert p_minority == pytest.approx(p, rel=0.05)

@pytest.mark.errors
def test_oversample_minority_class_high_p(data):
    with pytest.raises(ValueError) as e:
        sample.oversample_minority_class(data, 'y', 1.5)
    assert "Proportion out of bounds" in str(e.value)

@pytest.mark.errors
def test_oversample_minority_class_binary(data):
    with pytest.raises(ValueError) as e:
        data_ = data.loc[data['y'] == 1]
        sample.oversample_minority_class(data_, 'y', 0.5)
    assert "Binary outcome expected" in str(e.value)