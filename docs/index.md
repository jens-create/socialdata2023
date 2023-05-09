
# Welcome to our webpage on Making NYC Streets Safer!

Did you know that every year, thousands of traffic accidents occur on the streets of New York City, causing injuries and fatalities to drivers, passengers, and pedestrians alike? These accidents not only impact the lives of those involved but also affect the overall safety and well-being of our city.

In this page, we will explore the latest traffic accidents dataset and uncover insights that can help us make our streets safer. Together, we can work towards a future where accidents are less frequent, and everyone can feel confident and secure on NYC's roads. Let's get started!

# Summary statistics

<div class ="row" style="margin-top:20px;">
  <div class="col-md-12" style="text-align:center;">
          <p style="font-size: 30px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#008360 !important; margin-bottom: 2px; ">
               <font style="color:#83c3b2">131000</font> average crashes per year
          </p>

          <p
            style="font-size: 25px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#4c8f7e !important; margin-bottom: 2px;">
            <font style="color:#7fb9b3">86000</font> average crashes per year post-covid
          </p>
          <p
            style="font-size: 25px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#4c8f7e !important">
            <font style="color:#7fb9b3">71000</font> expected crashes in 2023

          </p>
        </div>

</div>

 <div class="row" style="margin-top:20px;">

        <div class="col-md-6" style="text-align: right;">
        <p
            style="font-size: 25px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#3c3c3c !important; margin-bottom: 2px;">
             All data
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important; margin-bottom: 2px;">
            <font style="color:#eaa969">167</font> deathly crashes per year
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important; margin-bottom: 2px;">
            <font style="color:#eaa969">29000</font> injury crashes per year
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important">
            <font style="color:#eaa969">102000</font> material damage crashes per year
          </p>

        </div>
        <div class="col-md-6" style="text-align: left;">
        <p
            style="font-size: 25px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#3c3c3c !important; margin-bottom: 2px;">
             Since 2020
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#ff5d49 !important; margin-bottom: 2px;">
            <font style="color:#ff8e7f">183</font> deathly crashes per year
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important; margin-bottom: 2px;">
            <font style="color:#eaa969">28500</font> injury crashes per year
          </p>
          <p
            style="font-size: 20px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important">
            <font style="color:#eaa969">57000</font> material damage crashes per year
          </p>

        </div>
      </div>



Artikel der beskriver hvorfor at tallet af ulykker er faldet efter april 2020:https://nyc.streetsblog.org/2020/04/03/nypd-gives-a-few-details-of-new-no-report-crash-policy/

(skyldes at politiet ikke længere rapporterer 'små' ulykker)


## Boxplot

{% include boxplot_collisions_per_day.html %}


## Time series x2
Not currently working with the setup...


 <div class="row" style="margin-top: 10px;">
  <div class="col-sm-12">
    <button type="button" class="btn btn-primary btn-circle shadow-none" id="basics"
      style="border-radius: 20px !important; background-color: #83c3b2
      ; border-color: #ffffff; padding-left: 20px; padding-right: 20px; margin-right: 10px; margin-top: 10px; color:white">Basics</button>
    <button type="button" class="btn btn-primary btn-circle shadow-none" id="ym"
      style="border-radius: 20px !important; background-color: #ffffff; border-color: #ffffff; padding-left: 20px; padding-right: 20px; margin-top: 10px;color:black">Yearly
      and Monthly Patterns</button>
    <button type="button" class="btn btn-primary btn-circle shadow-none" id="wh"
      style="border-radius: 20px !important; background-color: #ffffff; border-color: #ffffff; padding-left: 20px; padding-right: 20px; margin-top: 10px;color: black;">Weekly
      and Hourly Patterns</button>
  </div>
</div>

<div id="div_basics">
  BASICS
</div>

<div id="div_ym" style="display: none;">
{% include time_series_plot1.html %}
</div>

<div id="div_wh" style="display: none;">
{% include time_series_plot2.html %}
</div>

# Where in NYC do Traffic Incidents Occur?

### Traffic unsafety by borough
Below map compares how each borough in NYC is affected by traffic incidents overall, which is reflected in different persepectives such as area, population and severity of accidents.
{% include nyc_accidents_map.html %}

### Dangerous locations
In below map, we dive into specific trafic locations to identify where the traffic is most dangerous and thus where to prioritize safety enhancing initiatives for the people of NYC.
{% include accidents_locations_map.html %}


## Most dangerous areas in NYC

### Atlantic Avenue in Brooklyn
Atlantic Avenue in Brooklyn is the most dangerous street in New York City. It has the highest number of accidents, injuries, and fatalities of any street in the city. The street is a major thoroughfare that runs through several neighborhoods, including Bedford-Stuyvesant, Crown Heights, and Prospect Heights. It is also home to many businesses and residential buildings, making it a popular destination for pedestrians and cyclists. However, the street lacks adequate infrastructure for these users, with narrow sidewalks and bike lanes that are often blocked by parked cars or delivery trucks. This leads to conflicts between different modes of transportation, resulting in collisions and injuries.


An article from 2021, [SAFETY THIRD: Hit-and-Run Driver Kills Deaf Man on Notorious Speedway that DOT Failed to Fix](https://nyc.streetsblog.org/2021/10/16/safety-third-hit-and-run-driver-kills-deaf-man-on-notorious-speedway-that-dot-failed-to-fix/), sheds light upon the fact there has been renovation projects on improving the safety of `Atlantic Avenue` since 2014. The project, which aimed to improve safety for pedestrians and cyclists, involved adding high visibility crosswalks and curb extensions, but critics state that it has not fundamentally altered the geometry of the street or provided traffic calming measures. The article argues that despite the renovation, the number of injuries on the roadway has remained high, and the project's Phase II does not even have funding. Thus, we highly recommend that the city should prioritize the renovation of Atlantic Avenue to improve the safety of the street.


# Investigating the causes of accidents

Crashes on NYC streets are caused by various factors, some of which are more obvious than others. It could be a driver's distraction, fatigue, or even aggressive behavior. Pedestrians who jaywalk or cyclists who ride recklessly can also contribute to crashes.

This section will explore the different factors that contribute to accidents and how they vary depending on the the severity and type of transportation method. We will also look at how these factors have changed over time. That way, we can better understand what causes crashes and how we can prevent them from happening in the future.


Ideas:
- What are the most common factors that contribute to accidents? - OK
- How do these factors vary depending on the severity of the accident? - OK
- How do these factors vary depending on the type of transportation method? - OK
- How have these factors changed over time?
- What can we do to prevent these factors from happening in the future? - OK

## The most common factors that contribute to accidents

The following chart shows the top 8 factors that contribute to accidents in NYC for the three categories.

<div class="col-md-12">
{% include factor_plot.html %}
</div>

<div id="tab-content">
  <!-- Content for the tabs will be added here -->
  Driver inattention/distraction is the leading contributing factor in material damage-only accidents, accounting for over 54,681 crashes. This is likely due to the fact that a split second of inattention can easily lead to subsequent actions that result in a collision with another car or object.
  Following too closely is the second most common contributing factor, with approximately 14,369 accidents. Other common factors include passing too closely, improper passing or lane usage, backing unsafely, and failure to yield right-of-way. These factors may result from various causes, such as drivers attempting to pass or change lanes without signaling or checking blind spots, or backing up in areas with limited visibility. They may also occur when drivers misjudge the speed or distance of other vehicles, fail to properly anticipate their movements, or use lanes inappropriately. By identifying these factors and developing targeted strategies to reduce their occurrence, we can improve traffic safety and reduce the number of material damage-only accidents.
</div>


### Recommendation suggestions:
Based on the analysis of the three plots, there are several recommendations that could be made to improve road safety in New York City:

- Address driver inattention and distraction: This is the leading contributing factor to both material damage-only accidents and pedestrian fatalities, and is a common factor in crashes involving injuries to motorists, cyclists, and pedestrians. Strategies to address this issue could include increased public education campaigns, stricter enforcement of distracted driving laws, and the development and promotion of new technologies that reduce driver distraction.

- Improve pedestrian safety: Pedestrians are disproportionately affected by crashes leading to injuries and fatalities, and are often the victims of crashes involving failure to yield right of way. To address this issue, policies could focus on improving pedestrian infrastructure, such as adding more crosswalks and pedestrian signals, and redesigning streets to slow down traffic and increase visibility.

- Address speeding: Unsafe speed is the leading contributing factor to fatal crashes, particularly among motorists. Strategies to address this issue could include stricter enforcement of speed limits, the use of automated speed cameras, and roadway design changes such as road narrowing or speed humps.

- Focus on vulnerable road users: Cyclists and pedestrians are particularly vulnerable to injury and death in crashes, and thus policies could be implemented to protect these users. For example, this could include the promotion of protected bike lanes and the implementation of pedestrian-friendly designs such as sidewalks, crosswalks, and traffic calming measures.

Overall, a multi-faceted approach is needed to improve road safety in New York City, involving collaboration between policymakers, law enforcement agencies, transportation professionals, and the general public. By addressing the contributing factors to crashes, particularly those that result in injuries and fatalities, the city can work towards a safer and more sustainable transportation system.




## How do these factors relate to each other?

![Vehicle 1 factor vs Vehicle 2 factor](/assets/top_8_contributing_factors.png)


The plot includes the top nine contributing factors, with the size of the circle indicating the number of crashes and the color indicating the number of injuries or deaths.

The plot reveals several important insights. Firstly, crashes involving driver inattention/distraction for both vehicle 1 and vehicle 2 have the highest crash count and are associated with the highest number of injuries and deaths. This highlights the importance of addressing driver inattention and distraction in efforts to make New York City roads safer.

Secondly, the diagonal items of the scatter plots, which indicate when the same contributing factor is listed for both vehicle 1 and vehicle 2, are more frequent and more dangerous in terms of injuries and deaths. This finding suggests that when both drivers are engaging in the same risky behavior, the consequences are more severe.

Additionally, the plot shows that crashes involving unsafe speed and failure to yield right of way, as well as crashes involving unsafe speed and traffic control disregarded, are not highly frequent but are very dangerous. These factors may require additional attention and intervention to prevent crashes from occurring.

Finally, the plot reveals that crashes involving backing unsafely are relatively rare and rarely result in injuries or deaths. This suggests that addressing this contributing factor may not be as high of a priority as others when it comes to improving road safety in New York City.

Overall, this scatter plot provides valuable insights into the correlation between contributing factors in crashes, highlighting the importance of addressing driver inattention and distraction and the need to focus on risky behaviors when both drivers are engaging in them. By taking these insights into account, policymakers and safety advocates can make more informed decisions about how to improve road safety in New York City.

## Conclusion on factors...

To conclude on the four plots, the policymakers in NYC should focus on addressing the most common contributing factors to crashes and the factors that lead to the most severe crashes.

The leading contributing factor to material damage-only crashes is driver inattention/distraction, which accounted for over 54,000 crashes. This highlights the need for increased awareness and enforcement of distracted driving laws, as well as efforts to educate drivers on the dangers of distractions while driving. Additionally, following too closely is the second most common contributing factor and should be addressed through education and enforcement of safe following distances.

When it comes to crashes that lead to injuries or deaths, policymakers should focus on addressing unsafe speed, driver inattention/distraction, and failure to yield right-of-way. These factors are the top three contributing factors in crashes leading to injuries or deaths. Reducing speed limits and increasing enforcement of speed laws could be effective in reducing crashes caused by unsafe speed, while increasing education and awareness campaigns around distracted driving could help combat driver inattention/distraction.

Finally, policymakers should also address the correlation between the contributing factors in crashes. The analysis of the correlation between contributing factors reveals that diagonal items of the scatter plots are more frequent and also more dangerous, indicating that the combination of certain factors may lead to more severe crashes. Policymakers should take a holistic approach to addressing contributing factors, taking into account the interplay between different factors and how they contribute to crashes.


<script>

  // Event listener to buttons

  $(document).ready(function () {

    document.body.style.zoom = 1


    $("#basics").click(function () {
      $("#div_basics").show();
      $("#div_ym").css('display', 'none');
      $("#div_wh").css('display', 'none');
      $("#ym").css('color', 'black');
      $("#ym").css('background-color', 'white');
      $("#wh").css('color', 'black');
      $("#wh").css('background-color', 'white');
      $("#basics").css('background-color', '#83c3b2');
      $("#basics").css('color', 'white');
    })

    $("#ym").click(function () {
      // #83c3b2
      $("#div_ym").show();
      $("#div_basics").css('display', 'none');
      $("#div_wh").css('display', 'none');
      $("#basics").css('color', 'black');
      $("#basics").css('background-color', 'white');
      $("#wh").css('color', 'black');
      $("#wh").css('background-color', 'white');
      $("#ym").css('background-color', '#83c3b2');
      $("#ym").css('color', 'white');

    })

    $("#wh").click(function () {
      // #83c3b2
      $("#div_wh").show();
      $("#div_ym").css('display', 'none');
      $("#div_basics").css('display', 'none');
      $("#basics").css('color', 'black');
      $("#basics").css('background-color', 'white');
      $("#ym").css('color', 'black');
      $("#ym").css('background-color', 'white');
      $("#wh").css('background-color', '#83c3b2');
      $("#wh").css('color', 'white');

    })
  })


</script>
