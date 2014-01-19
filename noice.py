#!/usr/bin/env python3

import praw, sys, time

reddit = praw.Reddit('Noice Correction Bot by /u/5paceManSpiff')

def handle_ratelimit(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
            break
        except praw.errors.RateLimitExceeded as error:
            print('\tSleeping for %d seconds' % error.sleep_time)
            time.sleep(error.sleep_time)

def main():
    if len(sys.argv) < 3:
        print('No username or password found')
        return

    reddit.login(sys.argv[1], sys.argv[2])
    all_comments = [x for x in reddit.get_comments('all')]

    replies = 0
    already_done = set()
    for comment in all_comments:
        if comment.id not in already_done:
            if 'Nice' in comment.body or 'nice' in comment.body:
                handle_ratelimit(comment.reply, 'noice m8')
                replies += 1
                already_done.add(comment.id)
            elif 'What?' in comment.body or 'what?' in comment.body:
                handle_ratelimit(comment.reply, 'u wot m8?')
                replies += 1
                already_done.add(comment.id)

    print(str(replies))

if __name__ == '__main__':
    sys.exit(main())
