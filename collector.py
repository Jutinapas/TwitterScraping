import twint
import json

# Set up TWINT configonfig
config = twint.Config()

hashtag = "#JamesGunn"
since = "2018-1-1"
until = ""
limit = 100000
lang = "en"
file = "json"

config.Search = hashtag
config.Since = since
config.Limit = limit
config.Lang = lang

# Custom output format
config.Custom["tweet"] = ["hashtags"]
if file == "json":
    config.Store_json = True
elif file == "csv":
    config.Store_csv = True
directory = "%s_%s_%d_%s" % (hashtag, since, limit, file)
config.Output = directory

# Start searconfigh
twint.run.Search(config)

# dict = {}
#
# directory = "#PS4_2018-1-1_10000_json"
# path = "./" + directory + "/tweets.json"
# with open(path, encoding="utf8") as f:
#     for line in f:
#         j_content = json.loads(line)
#         for hashtag in j_content["hashtags"]:
#             if hashtag in dict:
#                 dict[hashtag] += 1
#             else:
#                 dict[hashtag] = 1
#
# print(sorted(dict.items(), key = lambda kv: kv[1], reverse = True))
# print(len(dict))
