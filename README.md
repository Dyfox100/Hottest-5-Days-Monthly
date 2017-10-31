Description:
  This program takes in the .csv file included which contains daily weather data for Boulder Colorado from 1897 to present.
  It cleans up the year and month format (originally the months with a numeric value greater than 9
  reset with numeric values starting at zero and another year with the same value was added
  ex. December 1979 originally was 1979 1, 2; now December 1979 = 1979, 12), then finds the mean of the hottest five daily high temps for     each month.It then exports the results and the clean original data to a .csv.
  
Compilation:
  Compile using python 3 with numpy and pandas modules. You will need to run it with the python command.
