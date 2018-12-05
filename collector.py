import twint
import json

# Set up TWINT configonfig
config = twint.Config()

hashtag = "#sundayfunday"
since = "2018-5-12"
sunday = "2018-5-13"
until = "2018-5-15"
# limit = 10000
# lang = "en"
file = "json"

config.Search = hashtag
config.Since = since
config.Until = until
# config.Limit = limit
# config.Lang = lang

# Custom output format
config.Custom["tweet"] = ["hashtags"]
if file == "json":
    config.Store_json = True
elif file == "csv":
    config.Store_csv = True
directory = "SundayFunday/%s" % (sunday)
config.Output = directory

# Start searconfigh
twint.run.Search(config)
