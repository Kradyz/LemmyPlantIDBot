# LemmyPlantIDBot


This is a Lemmy bot to identify plants from images posted to mander's plantid community.

The original bot was this one: https://github.com/stark1tty/plantid-mander.xyz-bot

However, the websockets were deprecated in favor for HTTP requests.

This implementation uses cURL to achieve the same effect. 

For automation, a cron job is used to run this python script every minute.


# Deployment

On linux, you can create a cron job ('crontab -e') as follows:

`* * * * * /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py`

This cron job will check for new posts every minute. A disadvantage is that if two new posts are created within a minute, one of those posts will be skipped. 

Cron is unable to work with sub-minute resolution, but it is possible to set multipl cron jobs offset by a few seconds (from: https://stackoverflow.com/questions/9619362/running-a-cron-every-30-seconds).

For example, this cron job make the bot check every 10 seconds:

`* * * * * /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py`
`* * * * * (sleep 10; /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py)`
`* * * * * (sleep 20; /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py)`
`* * * * * (sleep 30; /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py)`
`* * * * * (sleep 40; /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py)`
`* * * * * (sleep 50; /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py)`
