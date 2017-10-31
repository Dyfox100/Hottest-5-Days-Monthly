

import pandas as pd
import numpy as np
import matplotlib as plt


def parseYearsAndMonths(row):
    if len(row["year"]) > 4:
        row["month"] += 10
        row["year"] = row["year"][0:4]
    row["year"] = int(row["year"])
    return row

def importAndClean():
    """Imports, drops nulls, and changes year month format to be numbers 1 through 12"""
    #loads
    climateDF = pd.read_csv("raw_climate_data.csv")

    #Drops -998 (null value)
    climateDF = climateDF[climateDF["t_max"] != -998]

    #resets indexes after dropping values
    climateDF.reset_index(drop=True, inplace=True)

    #drops documentation at end of file
    climateDF=climateDF.iloc[0:43397]
    
    #converts to string to check length and parse
    climateDF["year"].apply(lambda s: str(s))
    #runs parse function
    climateDF = climateDF.apply(lambda row: parseYearsAndMonths(row), axis=1)

    #Exports clean csv
    climateDF.to_csv("cleaned_climate_data_just_maxT.csv")

def hottest_Consecutive_5_Days_Mean_Monthly():
    """Finds the mean of the five hottest consecutive days of every month"""

    #loads clean data
    climateDFClean=pd.read_csv("cleaned_climate_data_just_maxT.csv")
    #gets rid of unnecessary columns
    climateDFClean = climateDFClean.iloc[:, 1:5]

    #creates list of year and month combos for our data
    yearsAndMonths = [[x, y]  for x in range(1897, 2018) for y in range(1, 13)]
    yearsAndMonths = yearsAndMonths[4:]

    #creates list for hottest 5 days info
    monthlyList = []

    #iterates through list of year/month combos
    for yearMonth in yearsAndMonths:
        #creates temp with just that month
        tempDf = climateDFClean[climateDFClean["year"] == yearMonth[0]]
        tempDf = tempDf[tempDf["month"] == yearMonth[1]]
        max5Days = 0
        #finds hottest five days
        for index in range(tempDf.shape[0]):
            just5 = tempDf.iloc[index:(index+5)]
            high5 = just5["t_max"].sum()
            if (high5 > max5Days):
                max5Days = high5
        #appends mean of hottest five days
        monthlyList.append([(np.mean(tempDf["year"])),(np.mean(tempDf["month"])), (max5Days/5)])

    #Creates dataframe, drops nan, converts year/month back to string, and writes to CSV
    monthlyHighestFive = pd.DataFrame(monthlyList, columns=["year", "month", "mean of 5 hottest consecutive days"])
    monthlyHighestFive.dropna(inplace=True, how="any")
    monthlyHighestFive = monthlyHighestFive.astype({"year": str, "month":str}, copy=False)
    monthlyHighestFive.to_csv("Highest 5 Consecutive.csv", index=False)


def main():
    importAndClean()
    hottest_Consecutive_5_Days_Mean_Monthly()

if __name__ == "__main__":
    main()
