import pandas as pd
import numpy as np

from nose import runmodule
from numpy.testing import assert_array_equal

from cframetools import crossmap


def dumtimes(x, y):
    return x * y


class TestCrossMap(object):

    def setup(self):
        self.a = np.arange(5).astype(int)
        self.b = np.arange(5).astype(int)
        self.aseries = pd.Series(self.a, index=['a', 'b', 'c', 'd', 'e'])
        self.aseries = pd.Series(self.b, index=['a', 'b', 'c', 'd', 'e'])

    def test_crossarray(self):
        dumtimes = lambda x,y: x * y  #noqa
        expected = np.outer(self.a, self.b)
        result = crossmap(self.a, self.b, dumtimes)
        assert_array_equal(expected, result)


if __name__ == '__main__':
    import sys
    argv = [__file__, '-vs', '-a', '!slow'] + sys.argv[1:]
    runmodule(argv=argv, exit=False)
