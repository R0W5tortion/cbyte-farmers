import sys, re, json, os

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
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        print("Invalid command or filename. Correct usage:")
        print("python main.py FILENAME.json")
        sys.exit(1)
    tweets = json.load(sys.argv[1])
    while True:
        print("1. Show 10 tweets with most RTs")
        print("2. Show 10 users with most tweets")
        print("3. Show 10 days with most tweets")
        print("4. Show 10 most used hashtags")
        print("5. Quit")
        opt = input().strip()
        if not opt.isdigit():
            print("Invalid input")
            continue
        opt_n = int(opt)
        if not (1 <= opt_n <= 5):
            print("Invalid input")
            continue
        if opt_n == 1:
            top10 = top10tweets(tweets)
            for tweet in top10:
                print("url:", tweet["url"])
                print(tweet["content"])
                print(tweet["retweetCount"], "retweets")
        elif opt_n == 2:
            top10 = top10users(tweets)
            for user, tweet_n in top10:
                print(f"user: {user}, {tweet_n} tweets")
        elif opt_n == 3:
            top10 = top10days(tweets)
            for date, tweet_n in top10:
                print(f"On {date} there were {tweet_n} tweets")
        elif opt_n == 4:
            top10 = top10hashtags(tweets)
            for hashtag, tweet_n in top10:
                print(f"hashtag #{hashtag} appeared on {tweet_n} tweets")
        elif opt_n == 5:
            break

if __name__ == "__main__":
    main()