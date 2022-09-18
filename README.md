
# Agux's Non Linear Plot Regressor

## Description
Tired of slow and paid heavy weight statistics apps for your simple regression tasks? Agux's Non Linear Plot Regressor is your solution for 1 variable non linear regression. You can use one of the many pre-loaded fitting functions or easily define your very own to suit your needs.
It is made with python libraries, is fast,  has intuitive interface, provides many metrics (R2, RMSE, Chi2) and parameter values standard deviations.
It uses scipy.optimize.curve_fit to make the iterative calculation by TRF method (Trusted Region). App commes with 4 different real life datasets that you can test.
<!-- ![screen-gif](./prueba_rando_creator.gif) -->
<!-- <img src="https://github.com/aguxone/agux_random_file_creator/blob/gif_storage/prueba_rando_creator.gif?raw=true" alt="agxu_rfc_gif" width="60%" height="40%"> -->
<img src="https://github.com/aguxone/agux_non_linear_plot_regressor/blob/gif-storage-branch/756x490.gif?raw=true" alt="agux_nlpr_gif" width="70%" height="40%">
<!-- <video src='https://user-images.githubusercontent.com/98858551/174418629-481619d3-27ed-48c0-b952-05b6239417b3.mp4'; width="100"; height="100"></video> -->
<!-- https://user-images.githubusercontent.com/98858551/174418629-481619d3-27ed-48c0-b952-05b6239417b3.mp4 -->
<!-- <video  style="display:block; width:10%; height:auto;" autoplay controls loop="loop">
       <source src=https://user-images.githubusercontent.com/98858551/174418629-481619d3-27ed-48c0-b952-05b6239417b3.mp4 type="video/mp4" />
</video> -->
<!-- <div style="width:100px ; height:100px>
       <video src='https://user-images.githubusercontent.com/98858551/174418629-481619d3-27ed-48c0-b952-05b6239417b3.mp4'></video>
<div/> -->

## Languages / Libraries used
- Python
- Matplotlib
- Numpy
- Scipy
- WxPython

## Downloading and Opening the app:
- You can download the source code by clicking on the green "Code" button on the upper section of this web page, or download an executable file for Windows in the <a href="https://github.com/aguxone/agux_non_linear_plot_regressor/releases">Releases</a> page at your right (it's inside the zip file).
- If using the source code, just run the .py file with a python interpreter (previously having installed python and the necessary libraries)
- If using a Windows standalone release, just open the .exe file , it has no dependencies at all (except for the included image files). The app was compiled with pyinstaller, so the app needs to load the python interpreter + libraries when opening; this process might take from 5 secs to 2 min depending on your computer (be patient if you think is not loading, but once loaded the app is quite responsive).

## Usage:
- Opening a file: Use the open button to choose a .csv or .txt file, and choose an adequate delimiter below. File must be a comma separated file (using comma, semicolon, space or tab as delimiter) and must have 2 or 4 columns. First column is for the independent variable (x) , second column for the dependent variable (y), and third and fourth columns are for x and y error estimates respectively (one x and one y error for each data instance).
- Error cols present? Constant errors? Using 2 columns file: If "Error cols present" is "No" the program will ask to assign a % of error to the x and y variables (defaults are X= 0% and Y= 5%), and it will assume you have only 2 columns with X and Y data. This assignment is optional, since it is only used to display error bars, and to calculate a coherent chi2 statistic. If both % are zero, bars will not be plotted and chi2 square statistic will give and "inf" value since it will have zero as denominator in the statistic quotient. Aditionally if "Constant errors?" is "Yes" the app will behave as already described but assigning the same absolute error to each instance of data (assigned by the user, but defaults are X=0 and Y= 0.5).
- Plotting the data and fits: Just use the "Plot" button in order to plot the loaded file. Each time you click on "Plot" or "Fit", a new plot will appear on the screen, coexisting with the previous plot. You can erase the plots by clicking on the "Clear" button (although it will clear all the plots). You can plot scatter points or a continuous plot by clicking on the appropiate boxes; nothing will show up until you click on "Plot" or "Fit". Parameter values and their standard deviations, Rsquared, RMSE and Chi2 statistics are displayed only for the latest fitted curve in the bottom right corner of the graphical interface, so be sure to write down the results if you need them before making a new fit.
- Custom Cuve Fit: In the "Choose fit curve" section you can select the "Custom" option and define your own curve, it is a requirement that you use python and numpy syntax, it has an "Instructions" button in order to succesfully fit your curve (don't worry it's quite simple). You can use up to 25 parameters, you can use the letters from a to z (except the x) and need to follow alphabetical order (e.g if you need 3 parameters you have to use "a,b,c" and not "a,b,d" or "c,b,a" ). The letter "x" will be the independent variable in your expression.
- Saving and navigating through the plot: The plot will feature 6 "widgets" or "icons" on it's bottom to interact with (matplotlib widgets). Hovering with the mouse cursor over the widgets will display a clear explanation of it's functionality; you'll be able to reset the view, to go back and forth to different zoom states, to zoom, and to save the plot as an image file with the last one. Be aware that the saved files are "renders" and that their resolution will be the one used currently by your display (vector graphics not supported for now), though you'll probably won't care too much about the resolution for this particular use case.

## Details about calculations:
- Itearative calculations for minimizing least squares are automated by scipy library (scipy.optimize.curve_fit) using Least Squares and TRF method. You can learn more in https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
- Chi2 is calculated by using the following formula:

     $$ \chi^2 = \sum_{i=1}^{n}  ( \frac{y_i - \hat{y}}{\sigma_i})^2 $$
     
Where y_i are the data points, y_hat is the predicted y point by the curve, and  sigma_i is the error estimate of the y_i value.
Degrees of freedom are calculated as DF = number of data point - number of parameters of the fitted curve. The "Reduced Chi2" value shown in the app is the Chi2 statistic divided by DF. Have in mind that Chi2 distribution's expected value (or mean) is exactly the DF value which is useful for "goodness of fit" conclusions.

- RMSE is calculated by using the following formula:

     $$ RMSE = \sqrt{ \frac{1}{n} \sum{(y_i - \hat{y})^2}} $$

Where y_i are the data points, yhat is the predicted y point by the curve, and  sigma_i is the error estimate of the y_i value.

## Example datasets:
Non linear regression is a tiny art where you need to know a bit about your function in order to use adequate initial parameters for the alogorithm to converge to a coherent answer. Change the following initial parameters for the provided example datasets to find an adequate curve:
- Gaussian: b=2
- Dampened Sine : d=15 , e =2.4
- Sine: a=4 , b=9
- glutation : defaults are ok for exponential curve

## Changelog:
From 1.0.0 to 1.1.0:
- Added support for high dpi displays on windows
- Added constant error option in adition to % error
- Changed sash position relative to display size
- Added "About this app" button and dialog.

## About the app:
- Made with love for nerds by Agustín Alejo García, degree/master of science in Chemistry (2022)
- From University of Buenos Aires (Argentina), Faculty of Exact and Natural Sciences.
- Contact: aguxgarcia@hotmail.com
- This app is open source and free for personal or educational use.
But it's also free to say thanks and/or reference the author if you use it or find it useful for any use case.
