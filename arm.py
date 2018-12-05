from apyori import apriori
from pprint import pprint
import ast

filename = "./SundayFunday/2018-11-25/tweets.json"
with open(filename, encoding='utf-8') as tweets:
    data = [ast.literal_eval(tweet)['hashtags'] for tweet in tweets]
asso = list(apriori(data, min_support=0.015, min_confidence=0.75))
for rule in asso:
    print(rule.items)
