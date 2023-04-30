---
layout: page
title: A 5-YEAR PRIORITIZATION PROGRAM 2018-2023
---

In recent years, San Francisco Police Department (SFPD) has struggled to allocate resources efficiently and adequately for controlling criminal activities in the city.
To overcome this challenge, the Social Data Dream Team conducted an analysis using criminal data records from SFPD in the period of 2003-2017 to provide insights into typical patterns and the development of crime. The results of the analysis set the foundation for a new prioritization program that will run the coming five years, 2018-2023.

The data set includes 2,084,466 incident records in total, and each incident is characterised by 35 features including date, time, category, location, district, etc. In total the crimes are categorized into 37 categories.

## Property- & Violence Related Crime
The main focus of this analysis are two critical groups of activities: *property-related* and *violence-related* crimes respectively. Property-related crimes comprise burglary, vehicle theft, arson, larceny/theft, vandalism, trespass and trea. From 2003 until 2018 there has been recorded 812,501 property crimes. Violence-related crimes comprise sex offences (forcible), sex offences (non-forcible), assault and robbery, for which 225,089 records have been registered throughout the same period.

As larceny/theft, vehicle theft, vandalism and burglary accounts for more than 90% of the crimes we choose to omit trea and arson from our analysis.

**I THINK WE SHOULD DO THIS (above). Så behøver vi ikke at lave en normaliseret time plot, og vores story handler alligevel om larceny - særligt trea ser også meget dum/sjov ud i vores sidste plot. **

Below figure shows the historical development of crime frequency of each individual category within the two groups in addition to the overall development of both groups.

{% include time_series_plot.html %}
<center> <em> Development of property- and violence-related crimes from 2003 to 2018. First two tabs shows how each category within property and violence crimes develops and the third shows the aggregated number of crimes for the two groups. </em> </center><br>


During the entire period, a significantly larger frequency of property-related crime has been registered in San Francisco compared to violence-related crime. The most dominating crime activity is *larceny/theft*, which seems to have been rapidly increasing in frequency since 2011. The overall development of property related records seems to be **heavily impacted by** the development of **larceny/theft records, hence SFPD should define a strategy targeting this category** in order to combat the overall increasing rate of crime in the dominating property-related crimes.  In regards to the violence-related crimes, it can be seen that each category fluctutates around the same value throughout the years. Thus, it can be concluded that the SFPD have been able to keep the violence-related crimes at check mate - which is in alignment with the rest of the country ([bbc.com](https://www.bbc.com/news/57581270)).



## Critical Districts
To allow the management of the SFPD to know which district of San Francisco to focus on, an analysis of the likelihood of crime per district is is carried out. To introduce the least bias in the findings, the crime frequency is normalized by dividing with the district population. **refence til hvor vi får ekstra data fra**.


{% include map.html %}
<center> <em> Cloropleth map showing the normalized number of *property-related*, *violence-related* and *larceny/theft* crimes for the San Francisco districts. Depending on browser the plot may at first show all three cloropleth maps on top of each other - please actively select one of the options. </em> </center><br>


Analyzing the crime occurrences relative to the population within each district shows that the critical challenge of larceny/theft is highly dominating in especially the Southern district and also in the adjacent districts; Central, Northern and Tenderloin. This is interesting. As these areas are the most populated areas of San Francisco the crime frequency is the heaviest 'normalized' by the high population number - but still these areas encounter the most crime. **Giver det mening hvad jeg skriver**? Interestingly, but expected, the larceny/theft crime category dominates the property-related crime group as the cloropeth maps of the two are very similar. It is also clear that the mentioned districts are most pre-dominant when it comes to violence-related crimes.

## Critical Times during the Weekend
**Man kunne evt. gøre vores fortælling stærkere ved kun at kigge på ovennævnte districts**
To further investigate when the police officers of the Southern, Central, Northern and Tenderloin districts should be on the streets an analysis of the crime times are carried out. The analysis includes the selected crime categories for both crime groups as there may be overlap between them, thus, several crime categories can be combatted with the same strategy.


{% include plot3.html %}
<center> <em> Normalized count for different crime categories within the two crime groups throughout the week. </em> </center><br>

Looking at the property crimes it is clear that burglary have the most similar crime pattern compared to larceny/theft. They both experience the most 'activity' during the day hours and very little during the night. Vandalism and vehicle theft are somewhat similar but experiences a steady increase in crime frequency during the day, whereas the first two are more 'bell' shaped. The violence-related crimes are similar - they also increase during the day and peaks at midnight and in the weekend. Thus, if SFPD wishes to actively combat the larceny/theft crime category they can expect to also combat the burglary category.




## Strategy Proposal for SFPD

The Social Data Dream Team proposes the following 5-year prioritization program for the management of San Francisco Police Department. The department should prioritize resources towards addressing property-related crimes, especially larceny/theft. The department should also consider allocating resources based on the occurrence of crime relative to the population within each district, with a particular focus on the Southern district and adjacent districts, including Central, Northern, and Tenderloin. In general, we advise the department to have a dynamic and data-driven approach to tackling criminal activities, and the department should continually monitor and adjust strategies based on changes in patterns and trends of criminal activity.


**Are we doing this (from assignment description): It is a plus if you can back up some of your findings with external sources, such as news stories from the area, looking up which building is located at some set of lat,lon coordinates, or similar. (So when you see something happening at some time/place in the data, see if you can understand it more deeply by investigating outside the dataset.)** Do we care?
