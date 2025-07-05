#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "29378064"))
    API_HASH = os.environ.get("API_HASH", "44cf2bea8cbe0ec4e383427aab3fa934")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7500009525")
