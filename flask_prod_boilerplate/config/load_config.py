# -*- coding: utf-8 -*-
import os

import config.config as configr
import util.constants as const


def load_config(app):

    print("Loading configuration...")
    _env = os.environ.get(const.ENV, const.DEVELOPMENT)
    if _env == const.PRODUCTION:
        app.config.from_object(configr.ProductionConfig())
    elif _env == const.DEVELOPMENT:
        app.config.from_object(configr.DevelopmentConfig())
    else:
        app.config.from_object(configr.DevelopmentConfig())
