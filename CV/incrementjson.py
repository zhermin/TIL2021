import json
data = json.load(open('labels.json'))
print(data['images'][0])
print(data['annotations'][0])

for i in range(len(data['images'])):
  data['images'][i]['id'] += 10000

for i in range(len(data['annotations'])):
  data['annotations'][i]['id'] += 10000
  data['annotations'][i]['image_id'] += 10000

print(data['images'][0])
print(data['annotations'][0])

out = 'labels_new.json'
with open(out, 'w') as f:
  json.dump(data, f)