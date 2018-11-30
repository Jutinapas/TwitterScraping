import json
import pickle

directory = "#JamesGunn_2018-1-1_100000_json"

path = "./" + directory + "/tweets.json"
target = "./" + directory + "/hashtagsList.txt"

dict = {}

with open(path, encoding="utf8") as f:
    hashtags = {}
    for line in f:
        j_content = json.loads(line)
        for hashtag in j_content["hashtags"]:
            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1

    hashtags = sorted(hashtags.items(), key = lambda kv: kv[1], reverse = True)
    dict["len"] = len(hashtags)
    dict["hashtags"] = hashtags
    with open(target, "w") as file:
        file.write(json.dumps(dict))
