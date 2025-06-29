from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path


class PlotData:
    """Class for plotting data and saving the plot to a file."""

    def __init__(
        self,
        filename: Path,
        type: str = "line",
    ) -> None:
        """Initializes the PlotData class with a filename and plot type.

        Args:
            filename (Path): Path to save the plot.
            type (str): Type of plot to create. Options are 'line', 'scatter', or 'bar'.
        """
        self.filename = filename
        self.type = type

    def plot(
        self,
        x: np.ndarray,
        y: np.ndarray,
        title: str = "Plot",
        xlabel: str = "X-axis",
        ylabel: str = "Y-axis",
    ) -> None:
        """Plots the data based on the specified type.

        Args:
            x (np.ndarray): Data for the x-axis.
            y (np.ndarray): Data for the y-axis.
            title (str): Title of the plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
        """
        plt.figure(figsize=(10, 6))
        if self.type == "line":
            plt.plot(x, y, marker="o")
        elif self.type == "scatter":
            plt.scatter(x, y)
        elif self.type == "bar":
            plt.bar(x, y)
        else:
            raise ValueError("Unsupported plot type. Use 'line', 'scatter', or 'bar'.")

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(fname=self.filename, dpi=300)
        plt.show(block=True)
