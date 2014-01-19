#!/usr/bin/env python3

import praw, sys, time

def handle_ratelimit(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
            break
        except reddit.errors.RateLimitExceeded as error:
            print('\tSleeping for %d seconds' % error.sleep_time)
            time.sleep(error.sleep_time)

def main():
    r = praw.Reddit('Noice Correction Bot by /u/5paceManSpiff')
    r.login('noice_bot', '[insert password here]')
    all_comments = [x for x in r.get_comments('all')]

    replies = 0
    already_done = set()
    for comment in all_comments:
        if 'nice' in comment.body and comment.id not in already_done:
            handle_ratelimit(comment.reply, '*noice')
            replies += 1
            already_done.add(comment.id)

    print(str(replies))

if __name__ == '__main__':
    sys.exit(main())
