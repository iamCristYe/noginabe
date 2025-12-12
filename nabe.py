import requests

for i in range(130158 + 100, 130158 + 1000):
    # https://video-tvtokyo.imgix.net/noginabe/20251030/image/20251030_noginabe_01_a_129070.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251102/image/20251102_noginabe_01_a_128759.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251109/image/20251109_noginabe_01_a_129012.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251116/image/20251116_noginabe_01_a_129202.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251123/image/20251123_noginabe_01_a_129471.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251130/image/20251130_noginabe_01_a_129884.jpg
    # https://video-tvtokyo.imgix.net/noginabe/20251207/image/20251207_noginabe_01_a_130158.jpg
    url = f"https://video-tvtokyo.imgix.net/noginabe/20251214/image/20251214_noginabe_01_a_{i}.jpg"
    print(url)
    # continue
    r = requests.get(url)
    if r.status_code == 200:

        print(f"Found image {url}")
        exit()

    else:
        print(f"Image {i} not found (status code: {r.status_code})")
