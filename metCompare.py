# FN to compare vector and raster data 
# IN: raster, geometry
# Out: [R^2?]
import ee
ee.Initialize()

mrlc = ee.Image('USGS/NLCD/NLCD2011')
thing = ee.FeatureCollection('ft:15DHxXvvrtYiI_wsc7v7hLMi9UmM7dyokTgKyrl3D')

pointStats = mrlc.select('impervious').reduceRegions(
  collection=thing,
  reducer=ee.Reducer.first(), 
  scale=30
).getInfo()['features']
#print thing 
print pointStats

id, x, y, val = [ 
    (pt['properties']['native_id'], pt['geometry']['coordinates'][0], pt['geometry']['coordinates'][1], pt['properties']['first']) 
    for pt in pointStats 
    if 'first' in pt['properties'].keys()
][0]


#Map.addLayer(mrlc.select('impervious'));
#Map.addLayer(thing, {color:'FF0000'});
