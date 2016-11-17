# FN to compare vector and raster data 
# IN: raster, geometry
# Out: [R^2?]
import ee
ee.initialize()

mrlc = ee.Image('USGS/NLCD/NLCD2011')
thing = ee.FeatureCollection('ft:15DHxXvvrtYiI_wsc7v7hLMi9UmM7dyokTgKyrl3D')

pointStats = mrlc.select('impervious').reduceRegions({
  collection : thing,
  reducer : ee.Reducer.first(), 
  scale : 30
})
print thing 
print pointStats


#Map.addLayer(mrlc.select('impervious'));
#Map.addLayer(thing, {color:'FF0000'});
