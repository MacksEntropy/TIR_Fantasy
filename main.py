import pandas as pd
import numpy as np

class TIRFantasy:

    def load_data(self, race_data: str, runner_data: str) -> None:
        """Load data from external CSVs

        Args:
            race_data (str) : Path to CSV containing race data
            runner_data (str) : Path to CSV containing runner data
        """
        self.legs = pd.read_csv(race_data)
        self.runners = pd.read_csv(runner_data)

    def speed_score(self, goal_time : int, actual_time : int) -> float:
        """
        :param: goal_time (int) : The goal time for a given leg in seconds.
        :param: actual_time (int) : The race time for a given leg in seconds.
        """
        return (goal_time/actual_time)

    def pace_adherence(self, goal_pace : int, actual_pace : int) -> float:
        return ((actual_pace-goal_pace)/goal_pace)**2 + ((actual_pace-goal_pace)/goal_pace)
    
    def difficulty_score(self, rank : int) -> float:
        """ Calculate the difficulty score of a given leg based on the rank (column race data csv). Maps the rankings [1,36] to a 
        difficulty score [100,0].
        """
        return 100 - ((rank-1) * (8/7))

    def performance_score(self, speed_score : float, pace_adherence : float, difficulty_score: float) -> float:
        """
        Calculate overall score where speed score has a 25% weight, pace adherence has a 75% weight, and the composite score is weighted 
        by the difficulty score of a given leg.
        """
        return difficulty_score * ((0.25 * speed_score) - (0.75 * pace_adherence))
    
if __name__ =="__main__":
    tir = TIRFantasy()
    tir.load_data("dummy_race_data.csv", "runner_data.csv")