import sys, re

def top10tweets(tweets: list):
    top = []
    for tweet in tweets:
        if len(top) < 10:
            top.append(tweet)
            top.sort(key = lambda t: t["retweetCount"], reverse = True)
            continue
        if top[-1]["retweetCount"] < tweet["retweetCount"]:
            top.pop()
            top.append(tweet)
            top.sort(key = lambda t: t["retweetCount"], reverse = True)
    return top

def top10users(tweets: list):
    users = {}
    for tweet in tweets:
        user = tweet["user"]["username"]
        if user not in users:
            users[user] = 0
        users[user] += 1
    top = sorted(users.items(), key = lambda u: u[1], reverse = True)
    return top[:10]

def top10days(tweets: list):
    dates = {}
    for tweet in tweets:
        date = tweet["date"][:10]
        if date not in dates:
            dates[date] = 0
        dates[date] += 1
    top = sorted(dates.items(), key = lambda u: u[1], reverse = True)
    return top[:10]

def top10hashtags(tweets: list):
    hashtags = {}
    pattern = re.compile(r"#(\S+)")
    for tweet in tweets:
        for match in pattern.finditer(tweet["content"]):
            if match[1] not in hashtags:
                hashtags[match[1]] = 0
            hashtags[match[1]] += 0
    top = sorted(hashtags.items(), key = lambda u: u[1], reverse = True)
    return top[:10]

def main():
    pass