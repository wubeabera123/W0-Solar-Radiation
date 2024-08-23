import seaborn as sns
import matplotlib.pyplot as plt


class CorrelationHeatmap:
    def __init__(self, data):
        """
        Initialize the CorrelationHeatmap object with a dataset.

        :param data: A pandas DataFrame containing the data.
        """
        self.data = data

    def plot_correlation_matrix(self, columns, title='Correlation Matrix'):
        """
        Plot a correlation matrix for the specified columns of the dataset.

        :param columns: A list of column names to include in the correlation matrix.
        :param title: The title of the plot (optional).
        """
        plt.figure(figsize=(12, 8))
        correlation_matrix = self.data[columns].corr()
        sns.heatmap(correlation_matrix, annot=True,
                    cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title(title)
        plt.show()
