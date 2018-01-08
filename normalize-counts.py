from area import area
import json

source = "/Users/scottfarley/Documents/scratch/lwsc_with_combined.json"
target = open("/Users/scottfarley/Documents/lwcs/joined.geojson", 'w')

for line in open(source, 'r'):
    feature = json.loads(line)
    featureArea = area(feature['geometry'])
    normValue = int(feature['properties']['value']) / featureArea
    feature['properties']['value'] = int(feature['properties']['value'])
    feature['properties']['normValue'] = normValue
    target.write(json.dumps(feature) + "\n")
