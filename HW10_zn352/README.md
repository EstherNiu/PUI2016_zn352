## HW10 Assignment 2

### I used summer and winter data to run two analysis, as the seasonal decomposition plot in Assignment1 suggests (peak and dip periods).
- Summer data: July - September of year 2013, 2014 and 2015
- Winter data: January - March of year 2014, 2015 and 2016 

Year difference is due to date limitation of the original monthly citi bike ridership data. 
 
### Then I calculated the average ridership of summer/winter in all stations. 

Figure 1 & 2 shows there is difference in the **(1)active scale** and **(2)activity density** between two seasons: 
- In general, people ride more in summer.
- People living in upper Manhattan ride bikes in winter more than summer.

Figure 3 & 4 shows geographical relationship in the neighboring area, compared to Figure 5 which is the spatial auto-correlation plot of monthly Citi Bike ridership. 
- **Hot spot** (positive relationship) differs little between monthly, summer and winter in Manhattan.
- **Cold spot** (negative relationship) shows that winter has the highest area/amount of negative correlation, meaning during winter people ride bikes little and there are bigger difference in tracts. 
 
From the plots we can assume that: 
- Winter affects more in boroughs other than Manhattan, e.g. Brooklyn, possibly mean that people are less likely to use Citi Bikes in South area of NYC between Jan - March. 

 ![plot: my .bashrc](plots/HW10_summerlag_zn352.png)

Figure 1

![plot: my .bashrc](plots/HW10_winterlag_zn352.png)

Figure 2

![plot: my .bashrc](plots/HW10_summer_zn352.png)

Figure 3

![plot: my .bashrc](plots/HW10_winter_zn352.png)

Figure 4

![plot: my .bashrc](plots/HW10_monthly_zn352.png)

Figure 5
