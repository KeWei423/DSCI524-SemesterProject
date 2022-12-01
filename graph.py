from matplotlib import pyplot as plt
from fernet import fernet_key, Fernet

class plotting:
    def __init__(self, info, f) -> None:
        self.data = info
        self.key = f
    
    def plot_calories(self):
        # print("to plot calories ", self.data['calories'])
        dates = list(self.data['calories'].keys())
        values = list(self.data['calories'].values())
        values = [fernet_key.decrypt(value, self.key) for value in values]
        values = [int(x) for x in values]
        # print("values: ", values)
        fig = plt.figure(figsize=(8,5))
        plt.bar(dates, values, color='cyan', width = 0.5)
        plt.ylabel("Calories")
        plt.grid(axis='y')
        # plt.title("calory intake this week")
        # plt.show()
        plt.savefig('./dataVisuals/calories.png')
        return
    
    def plot_heart_rate(self):
        dates = list(self.data['rest_heart_rate'].keys())
        values = list(self.data['rest_heart_rate'].values())
        values = [fernet_key.decrypt(value, self.key) for value in values]
        values = [int(x) for x in values]
        fig = plt.figure(figsize=(8,5))
        plt.scatter(dates, values, color='pink')
        plt.ylabel("Average Resting Heart Rate BPM")
        plt.grid(axis='y')
        # plt.title("Average Resting Heart Rate this week")
        # plt.show()
        plt.savefig('./dataVisuals/heart_rate.png')
        return
    

    def plot_steps(self):
        dates = list(self.data['steps'].keys())
        values = list(self.data['steps'].values())
        values = [fernet_key.decrypt(value, self.key) for value in values]
        values = [int(x) for x in values]
        
        fig = plt.figure(figsize=(8,5))
        plt.bar(dates, values, color='lime', width = 0.5)
        plt.ylabel("steps")
        plt.grid(axis='y')
        # plt.title("Steeps Walked this Week")
        # plt.show()
        plt.savefig('./dataVisuals/steps.png')
        return
    
    def plot_sleep_time(self):
        dates = list(self.data['sleep_time'].keys())
        values = list(self.data['sleep_time'].values())
        values = [fernet_key.decrypt(value, self.key) for value in values]
        values = [float(x) for x in values]
        fig = plt.figure(figsize=(8,5))
        plt.bar(dates, values, color='royalblue', width = 0.5)
        plt.ylabel("sleep time (minutes)")
        plt.grid(axis='y')
        # plt.title("Sleep time this week")
        # plt.show()
        plt.savefig('./dataVisuals/sleep_time.png')
        return