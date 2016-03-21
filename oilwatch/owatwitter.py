
from twitter import *

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '45419796-60jLL6n1NvZFc3LijAx4X0j539WR0QFbaMUH7WfeC'
ACCESS_SECRET = 'VRQ0U2LrVvLKlyKHaNUUzB7zhUw6Smxpx5nkGa77oZQY6'
CONSUMER_KEY = '4WM3pmKdrwRUC467DR2pgTo7d'
CONSUMER_SECRET = 'AVfR9gNVfCEPOWF1Zwaf9kKxG83t3H2cWhHvbcjocBiQeHFxrd'


t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

print t.statuses.user_timeline(screen_name="oilwatchafrica1", count=1)

