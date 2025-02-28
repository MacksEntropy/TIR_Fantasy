import pandas as pd
import numpy as np
import re

class TIRFantasy:

    def load_data(self, race_data: str, runner_data: str) -> None:
        """
        Load data from external CSVs
        :param: race_data (str) : Path to CSV containing race data.
        :param: runner_data (str) : Path to CSV containing runner data.
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
        """
        :param: goal_pace (int) : The goal pace for a given runner in seconds.
        """
        return ((actual_pace-goal_pace)/goal_pace)**2 + ((actual_pace-goal_pace)/goal_pace)
    
    def difficulty_score(self, rank : int) -> float:
        """ Calculate the difficulty score of a given leg based on the rank (column race data csv). Maps the rankings [1,36] to a 
        difficulty score [100,60].
        """
        return 100 - ((rank-1) * (8/7))

    def performance_score(self, speed_score : float, pace_adherence : float, difficulty_score: float) -> float:
        """
        Calculate overall score where speed score has a 25% weight, pace adherence has a 75% weight, and the composite score is weighted 
        by the difficulty score of a given leg.
        """
        return difficulty_score * ((0.25 * speed_score) - (0.75 * pace_adherence))
    
    def is_valid_race_time(self, time : str) -> bool:
        """
        Validates if a given time is in the HH:MM:SS format.
        """
        if type(time) != str:
            return False
        p = r"^([0-1]\d|2[0-3]):([0-5]\d):([0-5]\d)$"
        return bool(re.match(p, time))
    
    def convert_race_time(self,race_time : str) -> int:
        """
        Converts the race time of a leg to seconds for further calculation.
        :param: race_time (str) : Time in the HH:MM:SS format.
        """
        if not self.is_valid_race_time(race_time):
            raise ValueError(f"Invalid Race Time : {race_time}")
        times = race_time.split(":")
        hours = int(times[0])
        minutes = int(times[1])
        seconds = int(times[2])
        return (hours * 3600) + (minutes * 60) + seconds
    
if __name__ =="__main__":
    tir = TIRFantasy()
    print(tir.convert_race_time("01:00:30"))