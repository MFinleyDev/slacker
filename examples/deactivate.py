#!/usr/bin/env python
"""List items in slack."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os
from slackerbeta import Slacker


def remove_user():
    """List channels & users in slack."""
    try:
        token = os.environ['SLACK_TOKEN']
        slack = Slacker(token)
        user_id = "" #user id



        response = slack.users.admin.deactivate(user_id)
        result = response.body
        print(result)
    except KeyError, ex:
        print 'Environment variable %s not set.' % str(ex)


if __name__ == '__main__':
    remove_user()
