import redis

import config

r = redis.Redis(config.REDIS_HOST, 
                config.REDIS_PORT, 
                password=config.REDIS_PASSWORD)
