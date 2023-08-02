# LemmyPlantIDBot


This is a Lemmy bot to identify plants from images posted to mander's plantid community.

The original bot was this one: https://github.com/stark1tty/plantid-mander.xyz-bot

However, the websockets were deprecated in favor for HTTP requests.

This implementation uses cURL to achieve the same effect. 

For automation, a cron job is used to run this python script every few seconds.
