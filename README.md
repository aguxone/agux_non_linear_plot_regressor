
# Agux's Non Linear Plot Regressor

## Description
Tired of slow and paid heavy weight statistics apps for your simple regression tasks? Agux's Non Linear Plot Regressor is your solution for 1 variable non linear regression. You can use one of the many preset fitting curves or easily define your very own to suit your needs.
It is made with python libraries, is fast,  has intuitive interface and provides many metrics (R2, RMSE, Chi2) and parameters values standard deviations.

<!-- ![screen-gif](./prueba_rando_creator.gif) -->
<img src="https://github.com/aguxone/agux_random_file_creator/blob/gif_storage/prueba_rando_creator.gif?raw=true" alt="agxu_rfc_gif" width="60%" height="40%">

## Libraries used
- Matplotlib
- Numpy
- Scipy
- WxPython

## Opening the app:
- If using the source, just run the .py file (previously having installed the necessary libraries)
- If using a windows standalone release, just open the .exe file , it was compiled with pyinstaller and it needs to load the python interpreter + libraries so this might take from 5secs to 2 min depending on your computer (be patient).

## Usage:
- Opening a file: Usen to open button to choose a .csv or .txt file, and choose the delimiter below. File must be a comma separated file (using comma or other delimiter) and must have 2 or 4 columns. First column is for the independent variable (x) , second column for the dependent variable (y), and third and fourth columns are for x and y error estimates respectively (one error per data instance).
- Using 2 columns file: The program will ask to assign a % of error to the x and y variables. This assignment is optional, since it is only used to display error bars, and to calculate a coherent chi2 statistic. Is both % are zero bars will not be plotted and chi2 square statistic will give and "inf" value.
- Plotting the data and fits: Just use the Plot button in order to plot the loaded file. Each time you click on plot or fit, a new plot will appear on the screen, coexisting with the previous plot. You can erase the plots by clicking on the "Clear" button (although it will clear all the plots). You can plot scatter points or a conituous by clicking on the appropiate boxes, nothing will show up until you click on "Plot".
