import csv
import pandas as p
import plotly.figure_factory as pff
import plotly.graph_objects as go
import statistics as s
import random as r

df = p.read_csv(
    "D:/(4) WhiteHatJr. Codes/Third Module/Sampling/Project/Medium csv/medium_data.csv")

reading_time = df["reading_time"].tolist()

figure = pff.create_distplot([reading_time], ["Results"], show_hist=False)

#figure.show()

population_mean = s.mean(reading_time)
population_sd = s.stdev(reading_time)

print()
print("The Old Mean is {mean}" .format(mean=population_mean))
print()
print("The Old Standard Deviaton {sd}" .format(sd=population_sd))
print()


def random_set_of_mean(counter):
    data_set = list()
    for d in range(counter):
        random_i = r.randint(0, len(reading_time) - 1)
        data_set.append(reading_time[random_i])
    mean_of_data_set = s.mean(data_set)
    return mean_of_data_set

def draw_figure(data_set_n):
    figure = pff.create_distplot([data_set_n], ["Results"], show_hist=False)
    figure.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 1.2], mode="lines", name="Mean"))
    figure.show()

def setup():
    list_of_means = list()
    for i in range(1000):
        set_of_means = random_set_of_mean(100)
        list_of_means.append(set_of_means)
    draw_figure(list_of_means)
    mean_of_everything = s.mean(list_of_means)
    final_sd = s.stdev(list_of_means)
    print("Mean of Sampling Distribution {moe}".format(moe=mean_of_everything))
    print()
    print("Standard Deviation of the Sampling Distribution {f}" .format(f=final_sd))
    print()

setup()