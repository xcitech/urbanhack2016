# urbanhack2016
## a part of GeoHackWeek2016

## Introduction 
Extreme heat is one of the deadliest climate hazards even though heat-related deaths are easily preventable. Disaster management and relief agencies need highly localized temperature information to target interventions, but often, the area of highest concerns lack local weather stations. 

Land-surface temperature can be remotely sensed at sub-kilometer scale, but isn't suitable for making health decisions. We aim to make use of this and other satellite data to estimate 2-meter air temperature on a sub-kilometer scale: 

$$ f \left( T_{land}, \epsilon, NDVI, p, h \right) = T_{air}

## Workflow
To do this analysis, we combine satellite data extracted at locations with air temperature observations into a Pandas data frame. Using Google Earth Engine's Python API, we read in satellite data for elevation $h$, emissivity $\epsilon$,land cover percent impervious $p$, and raw Landsat8 data. We use this latter data to calculate land surface temperature $T_{land}$, vegetation fraction $NDVI$. Time-series of these data is sampled at weather station locations, and appended to a Pandas dataframe. These functions and sample code are documented here. Some additional javascript functions for Google Earth Engine are found here.  

To train our regression model, we read $T_{air}$ in a Pandas dataframe. To limit computation time, we train the model on a small subset of data, in this case, the Los Angeles area. The code to find weather stations in a particular area can be found here. 

The regression model.... [Raj/Matt fill in here]

Our regression model produces coefficients $\beta_0, \beta_1, \beta_2, ...$ for a model of the form: 
$$ T_{air} = \beta_0 + \beta_1 T_{land} + \beta_2 \epsilon + \beta_3 NDVI + \beta_4 p + \beta_5 h $$
To produce our map of $T_{air}$, we upload these coefficients into Google Earth Engine's javascript GUI. We calculate 

Last, to make this data accessible to end users, we provide a function that computes the average air temperature at an area given a point. This allows users to estimate heat exposure in an area. 

## Future work/ to do
- add .gitignore
- calculate error in output
- add atmospheric water vapor correction for LST
- keep workflow in one location (notebook+ GEE transfer isn't automatic)

## Questions? 
Get in touch: 
regression analysis: Raj/Matt
data: Anna/Logan
spatial calculations/visualization: Manindar
