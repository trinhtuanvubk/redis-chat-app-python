import json
import math
import random

import bcrypt

from chat import demo_data
from chat.config import get_config

SERVER_ID = random.uniform(0, 322321)

redis_client = get_config().redis_client