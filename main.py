import pandas as pd
import numpy as np
import re

class TIRFantasy:

    def load_data(self, race_data: str, runner_data: str) -> None:
        """Load data from external CSVs
        
        :param race_data: Path to CSV containing race data.
        :type race_data: str
        :param runner_data: Path to CSV containing runner data.
        :type runner_data: str"""
        self.legs = pd.read_csv(race_data)
        self.runners = pd.read_csv(runner_data)

    def speed_score(self, goal_time : int, actual_time : int) -> float:
        """Calculate the speed score for a given leg.
        
        :param goal_time: Goal time for a given leg and runner in seconds.
        :type goal_time: int
        :param actual_time: Actual time for a given leg and runner in seconds.
        :type actual_time: int
        :return: The speed score for a given leg.
        :rtype: float"""
        return (goal_time/actual_time)

    def pace_adherence(self, goal_pace : int, actual_pace : int) -> float:
        """Docstring for pace_adherence
         
        :param goal_pace: The goal pace for a given leg and runner in seconds.
        :type goal_pace: int
        :param actual_pace: The aculat pace for a given leg and runner in seconds.
        :type actual_pace: int
        :return: The pace adherence for a given leg and runner.
        :rtype: float"""
        return ((actual_pace-goal_pace)/goal_pace)**2 + ((actual_pace-goal_pace)/goal_pace)
    
    def difficulty_score(self, rank : int) -> float:
        """Transforms the rank of a given leg into a scaling constant for the perfomance score calculation. Maps the rankings [1,36] to a 
        difficulty score [100,60].
        
        :param rank: An metric indexing the diffuculty of a given race leg.
        :type rank: int
        :return: The difficulty score for a given leg.
        :rtype: float"""
        return 100 - ((rank-1) * (8/7))

    def performance_score(self, speed_score : float, pace_adherence : float, difficulty_score: float) -> float:
        """Calculate performance score as described in the README.
         
        :param speed_score: The Speed score for a given leg and runner.
        :type speed_score: float
        :param pace_adherence: The pace adherence for a given leg and runner.
        :type pace_adherence: float
        :param difficulty_score: The diffuculty score for a given leg.
        :type difficulty_score: float
        :return: The performance score for a given leg and runner
        :rtype: float"""
        return difficulty_score * ((0.25 * speed_score) - (0.75 * pace_adherence))
    
    def is_valid_race_time(self, time : str) -> bool:
        """Validates if a given time is in the HH:MM:SS format. Used in convert_race_time method.
        
        :param time: Description
        :type time: str
        :return: Boolean indicating if a given race time is in the valid format.
        :rtype: bool"""
        if type(time) != str:
            return False
        p = r"^([0-1]\d|2[0-3]):([0-5]\d):([0-5]\d)$"
        return bool(re.match(p, time))
    
    def convert_race_time(self, race_time : str) -> int:
        """Converts the race time of a leg to seconds for further calculation.
        
        :param race_time: Time in the HH:MM:SS format.
        :type race_time: str
        :return: Time in seconds.
        :rtype: int"""
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