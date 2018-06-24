#!/usr/bin/env python
import pandas as pd

# We only need these attributes to contribute
attributes = [
    "Endurance", "Strength", 
    "Power", "Speed", 
    "Agility", "Flexibility", 
    "Nerve", "Durability", 
    "Hand-Eye Coordination", "Analytical Aptitude"
]

# Handles inputting for valid and invalid values.
def validInput(attr):
    inNum = 0
    while True:
        try:
            inNum = float(input("Enter a value for " + attr + ": "))
            if 0 <= inNum and inNum <= 10:
                break
        except ValueError:
            print("Invalid entry.  Please try again.")
    return inNum

def main():
    df = pd.read_excel("Toughest Sport by Skill.xlsx")
    attr_table = df[attributes]
    # Enter all relevant attributes
    inputs = {attribute:0.0 for attribute in attributes}
    for attribute in attributes:
        inputs[attribute] = validInput(attribute)
    user = pd.DataFrame(inputs, index=[0], columns = attributes)

    # Now perform the calculations to recommend a sport
    sportRes = {"Sport":df["Sport"].values, "MSE":[]}
    for i in range(len(df)):
        tmp = attr_table.iloc[i].subtract(user.iloc[0])
        sportRes["MSE"].append((tmp ** 2).sum())
    sportMetrics = pd.DataFrame(sportRes, columns=["Sport", "MSE"])
    inx = sportMetrics["MSE"].idxmin()
    print("We recommend {} as the ideal sport for you!".format(sportMetrics["Sport"][inx]))
        

if __name__ == "__main__":
    main()