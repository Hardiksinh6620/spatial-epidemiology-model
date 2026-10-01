import numpy as np
from src.core import incidence_rate,standardize,gravity_flow,moran_input
def test_rates_and_gravity():
    assert incidence_rate([10],[1000])[0]==1000
    assert gravity_flow(100,200,10)==200
    assert np.isclose(standardize([1,2,3]).mean(),0)
    assert moran_input([1,2],[100,100]).shape==(2,)
