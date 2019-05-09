import os
import requests
import grequests

# number of simultaneous downloads allowed
simultaneousDownloads = 6

# name of the video
name = 'video'
# .ts URL of the video, replace segment number with {0}
source_url = 'http://example.com/stream/segment-{0}-a.ts'

if not os.path.exists(name):
    os.makedirs(name)

keys = []
urls = []
for x in range(1,2000):
    filename = '{0}/{1:04d}.ts'.format(name, x)
    if os.path.isfile(filename):
        print 'skip', x
        continue

    urls.append(source_url.format(x))
    keys.append(x)

    if len(urls) == simultaneousDownloads:
        rs = (grequests.get(u) for u in urls)
        results = grequests.map(rs)
        for key, _result in enumerate(results):
            filename = '{0}/{1:03d}.ts'.format(name, keys[key])
            print urls[key], _result.status_code
            if _result.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(_result.content)
            else:
                # if error assume no more segment, or you can run this script again to make sure it's a permanent error
                exit()
        urls = []
        keys = []