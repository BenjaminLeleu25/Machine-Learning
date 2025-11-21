from pathlib import Path
from typing import Literal
import pandas as pd


class PreprocessData:
    """
    This class load the data, preprocess the data: fill nan values.
    """
    def __init__(self, path):
        self.path = path
        self.df = self.load_csv(path)


    def load_csv(self, path: Path | str) -> pd.DataFrame:
        """
        Load the csv and create 4 columns: day, week, month and year.

        Args:
            path (Path | str): The path to the dataframe

        Returns:
            The dataframe
        """
        df = pd.read_csv(
            path,
            sep=",",
            index_col=0,
            parse_dates=True
        )
        df.sort_index()

        df["day"] = df.index.day.astype("float64")
        df['week'] = df.index.isocalendar().week.astype("float64")
        df["month"] = df.index.month.astype("float64")
        df["year"] = df.index.year.astype("float64")

        return df


    def fill_nan_using_avg(
        self,
        df: pd.DataFrame,
        regex: str,
        duration: Literal["day", "week", "month", "year"] = "week"
    ) -> None:
        """
        Fill nan of a column of a dataframe by using
        the monthly average.
        df needs to have as an index "Location" and "month".

        Args:
            df (pd.DataFrame): a dataframe
            regex (str): The regex rule to select the desire columns
            duration (str, optional): The column we use to group by.
            Can be "year", "month", "week" or "day"

        Returns:
            pd.DataFrame: The filled dataframe
        """
        df_to_fill = df.filter(regex=regex)
        df_filled = df_to_fill.fillna(
            df_to_fill.groupby(["Location", duration]).transform("mean")
        )

        self.df.update(df_filled, overwrite=False)


    def fill_nan_using_rain(self) -> None:
        """
        Fill the columns 'RainToday' and 'RainTomorrow' from a main df.
        It uses the rule:
        - if Rainfall >= 1, then RainToday == "Yes" else "No"
        - if Rainfall_shifted >= 1, then RainTomorrow == "Yes", else "No"

        Returns:
            None
        """
        self.df["RainToday"] = self.df.apply(
            lambda x: "Yes" if x["Rainfall"] >= 1. else "No", axis=1
        )

        copy_df = self.df.copy()
        copy_df["Rainfall"] = copy_df["Rainfall"].shift(periods=-1)
        copy_df["RainTomorrow"] = copy_df.apply(
            lambda x: "Yes" if x["Rainfall"] >= 1. else "No", axis=1
        )

        self.df.update(copy_df["RainTomorrow"], overwrite=False)
