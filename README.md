# immo_eliza_Analysis

# Project Description
After the success of gathering nearly 20 housands of data about houses/apartments from the Immoweb website, we were given the opportunity to continue upon this project to clean and analyse the data and draw out interpretations.

# Program description (workflow)
Overall:  the workflow was different as we continued upon the csv file that we scraped in the previous stage, we checked the columns and whats obvious to select and what's obvious to delete, we tried to link variables together and draw out conclusions in terms of missing data and how can we replace them or to simply drop those data, after the analysis and purifying phase we started to find the correlation between the variables and most importantly what correlates to our main goal which is the price of the houses and we found out that the main role player is the living Area. ultimately we made different types of graphs that shows the ammount of prices for the most and the least expensive municipalities in belgium and the regions.

1. The program has different stages, and the coding changed from phase to another.

2. The first stage was to select the columns needed and to rename them accordingly, as well as dropping all the duplicate data, and then replacing the none numerical values such as Yes/No with numerical binary values 0/1. 

3. Then we went with cleaning Prices which was string value to extract the numbers and replace it by those extracted numbers.finally defining scale for some none numerical values such as kitchen type.

4. Next phase was about checking the outliers by drawing correlation graph to see if some data are in the valid range and if not it will be removed or replaced, depending on the data itself, then after the data is purified from outliers.

5. when the data became clean, we created a new column prices per meter square and also column Region for walloon, flanders, and Bruxelles for the zip-code that lies in those regions, and then finding the prices for the most and the least prices for the municipalities that lies in those regions as well as whole Belgium.
6. 
6.finally sketching the results in charts with all the information needed such as discription of the charts, legends, coloring and discription fo the y and x axis, it was done by matplotlib module.

# Installation
This project was done under jupyter notebook but can be run using python, but preferebly to be used with jupyter notebook.
Install libraries ( numpy, Regex, urllib, Pandas,matplotlib)


After opening the jupyter notebook, select cleaning.ipynb to load it and Run it inside the notebook window by clicking on Run!, its so staight forward.

```bash
cleaning.ipynb
```

# Usage
Make price predictions on real estate sales in Belgium.

The task is prepare the data by classifying, cleaning and make it ready for the final stage which is subsequently will be used to build a model for price prediction.

# Visuals


# Contributors
Said<br>
Volodymyr<br>
Raghini<br>
Mahmoud

# Timeline
- Duration: `3 days`
