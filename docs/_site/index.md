<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>


# Welcome to our webpage on Making NYC Streets Safer!

Did you know that every year, thousands of traffic accidents occur on the streets of New York City, causing injuries and fatalities to drivers, passengers, and pedestrians alike? These accidents not only impact the lives of those involved but also affect the overall safety and well-being of our city.

In this page, we will explore the latest traffic accidents dataset and uncover insights that can help us make our streets safer. Together, we can work towards a future where accidents are less frequent, and everyone can feel confident and secure on NYC's roads. Let's get started!
{% include boxplot_collisions_per_day.html %}
{% include time_series_plot1.html %}
{% include time_series_plot2.html %}

 <div class="row" style="margin-top:20px;">

        <div class="col-md-2">
        </div>
        <div class="col-md-4" style="text-align: right;">
          <p
            style="font-size: 15px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#008360 !important; margin-bottom: 2px;">
            <font style="color:#83c3b2">672000</font> bikes in the city
          </p>

          <p
            style="font-size: 10px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#008360 !important; margin-bottom: 2px;">
            <font style="color:#83c3b2">375 km</font> bike network
          </p>
          <p
            style="font-size: 10px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#008360 !important">
            <font style="color:#83c3b2">26%</font> bike modal share (constant drop since 2013)

          </p>

        </div>
        <div class="col-md-4" style="text-align: left;">
          <p
            style="font-size: 15px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important; margin-bottom: 2px;">
            <font style="color:#eaa969">29.1%</font> of car ownership
          </p>
          <p
            style="font-size: 10px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important; margin-bottom: 2px;">
            <font style="color:#eaa969">700 km</font> road network
          </p>
          <p
            style="font-size: 10px ;font-weight: 800 !important; font-family: 'Readex Pro', sans-serif; color:#c86501 !important">
            <font style="color:#eaa969">31%</font> car modal share
          </p>

        </div>
        <div class="col-md-2">
        </div>
      </div>



## Where in NYC do Traffic Incidents Occur?


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Interactive Map</title>
<script>
function update_map(map_name) {
    document.getElementById("map_iframe").src = "{{site.url}}/assets/" + map_name + ".html";
}
</script>
</head>
<body>
    <button onclick="update_map('temp_map_accidents_per_sqkm')">Accidents by Borough</button>
    <button onclick="update_map('temp_loc_map_All')">Accidents by Street Location</button>
    <iframe id="map_iframe" src="{{site.url}}/assets/temp_map_accidents_per_sqkm.html" width="100%" height="600" frameborder="0" style="border:0" allowfullscreen></iframe>
</body>
</html>



{% include nyc_accidents_map.html %}

and lets have a closer look at specific locations

{% include accidents_locations_map.html %}


## Investigating the factors that contribute to accidents

Crashes on NYC streets are caused by various factors, some of which are more obvious than others. It could be a driver's distraction, fatigue, or even aggressive behavior. Pedestrians who jaywalk or cyclists who ride recklessly can also contribute to crashes.

This section will explore the different factors that contribute to accidents and how they vary depending on the the severity and type of transportation method. We will also look at how these factors have changed over time. That way, we can better understand what causes crashes and how we can prevent them from happening in the future.


Ideas:
- What are the most common factors that contribute to accidents? - OK
- How do these factors vary depending on the severity of the accident? - OK
- How do these factors vary depending on the type of transportation method? - OK
- How have these factors changed over time?
- What can we do to prevent these factors from happening in the future?

### The most common factors that contribute to accidents

The following chart shows the top 8 factors that contribute to accidents in NYC for the three categories.

{% include factor_plot.html %}

<div id="tab-content">
  <!-- Content for the tabs will be added here -->
  {{ site.data.tab1.content }}
</div>





### How do these factors relate to each other?

![Vehicle 1 factor vs Vehicle 2 factor](/assets/top_8_contributing_factors.png)


**Forklaring**:

Ovenstående plot:

Viser top 8 årsager der er mest hyppige for ulykker. Størrelsen af cirklen indikerer hvor mange ulykker der er sket med den pågældende årsag og farven indikerer hvor mange der er såret eller døde i ulykken.

Der er mange pointer der kan drages fra plottet:
- Driver Inattention/Distraction er den hyppigste årsag til ulykker, og at det er den årsag der har flest sårede og døde i ulykkerne.
- Af en eller grund så hvis begge biler har samme årsag så er ulykken slemmere; er det fejlrapportering eller er det fordi at samme årsag er mere alvorlig hvis begge biler har hver deres årsag?
- Unsafe speed fremgår som ret slem i forhold til hvor få crashes.
- Backing unsafely er ikke slem...
