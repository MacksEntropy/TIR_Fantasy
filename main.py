import pandas as pd
import numpy as np

class TIRFantasy:

    def load_data(self, race_data: str, runner_data: str):
        """Load data from external CSVs

        Args:
            race_data (str) : Path to CSV containing race data
            runner_data (str) : Path to CSV containing runner data
        
        """
        self.legs = pd.read_csv(race_data)
        self.runners = pd.read_csv(runner_data)

    def calculate_speed_score(self, goal_time, actual_time):
        return (goal_time/actual_time) * 100

    def calculate_pace_adherence(self, goal_pace, actual_pace):
        return (1-((abs(actual_pace-goal_pace))/goal_pace)) * 100
    
    def calculate_difficulty_score(self, rank):
        """ Calculate the difficulty score of a given leg based on the rank (column race data csv). Maps the rankings [1,36] to a 
        difficulty score [100,0].
        """
        return (1 - ((rank - 1)/(36-1))) * 100

    def calculate_overall_score(self, speed_score, pace_adherence, difficulty_score):
        return difficulty_score * ((0.25 * speed_score) + (0.75 * pace_adherence)) / 100

if __name__ =="__main__":
    tir = TIRFantasy()
    tir.load_data("dummy_race_data.csv", "runner_data.csv")