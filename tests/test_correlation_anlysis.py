import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.correlation_analysis import CorrelationHeatmap

class TestCorrelationHeatmap(unittest.TestCase):

    def setUp(self):
        # Sample data to test the CorrelationHeatmap class
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': [2, 3, 4, 5, 6]
        }
        self.df = pd.DataFrame(data)
        self.correlation_heatmap = CorrelationHeatmap(self.df)

    def test_plot_correlation_matrix(self):
        try:
            # Test for plotting correlation matrix with columns 'A' and 'B'
            self.correlation_heatmap.plot_correlation_matrix(['A', 'B', 'C'])
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
