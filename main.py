import csv
import pandas

# # with open("weather_data.csv") as data:
# #     raw_data_list = data.readlines()
# #
# # print(raw_data_list)
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperatures = []
# #     for row in data:
# #         print(row)
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# # print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
#
# # print(round(average, 2))
# print(data["temp"].max())
# print(data["temp"].mean())
#
#
# # print(data["condition"])
# # print(data.condition)
#
#
# # Get data in the rows of data
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = (int(monday.temp) * 9/5) +32
# print(monday_temp)
#
#
#
# # Create data frame by yourselve
#
# data_dict = {
#     "students": ["Amy","James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
#
# print(data2)
# data2.to_csv("new_data.csv")
#
squerrels=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squerrels_colours = squerrels['Primary Fur Color']
print(squerrels_colours)

gray_ones=squerrels_colours.str.count("Gray")
gray_sum = gray_ones.sum()
print(f" Szare {gray_sum}")

red_ones = squerrels_colours.str.count("Cinnamon")
red_sum = red_ones.sum()
print(f"RED {red_sum}")

black_ones = squerrels_colours.str.count("Black")
black_sum = black_ones.sum()
print(f"BLACK {black_sum}")

squerrels_colours_count ={
    "Fur Color": ["grey", "black", "red"],
    "Count":  [f"{gray_sum}", f"{black_sum}", f"{red_sum}"]
    # "black": f"{black_sum}",
    # "grey": f"{gray_sum}",
    # "red": f"{red_sum}"
}
squerrels_colours_count_final = pandas.DataFrame(squerrels_colours_count)
print(squerrels_colours_count_final)
squerrels_colours_count_final.to_csv("numbers_of_the_sqirrels.csv")


