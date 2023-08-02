# LemmyPlantIDBot


This is a Lemmy bot to identify plants from images posted to mander's plantid community.

The original bot was this one: https://github.com/stark1tty/plantid-mander.xyz-bot

However, the websockets were deprecated in favor for HTTP requests.

This implementation uses cURL to achieve the same effect. 

For automation, a cron job is used to run this python script every few seconds.


# Deployment

On linux, you can create a cron job ('crontab -e') as follows:

`* * * * * /usr/bin/python3 /home/bots/PlantID/PlantIDBot.py`

This cron job will check for new posts every minute. A disadvantage is that if two new posts are created within a minute, one of those posts will be skipped. 
