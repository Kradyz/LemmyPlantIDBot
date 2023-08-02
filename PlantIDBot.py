import json
import os
from subprocess import Popen, PIPE
import requests

community_name = "plantid"                      # Community that the bot will operate on
instance_url = "https://mander.xyz"             # The instance where the bot lives
stickied_posts = 1                              # The number of stickied posts in the community
LEMMY_JWT =  ""                                 # The auth token for the bot
PLANTNET_API_KEY = ""                           # The free API-key from plantnet.org
OLDID_FOLDER_PATH = ""                                 # Folder where the file 'old.txt' that contains the previous newest post ID will be stored

def getNewestPost():
 command = f"curl -s '{instance_url}/api/v3/post/list?community_name={community_name}&sort=New'"
 stdout = Popen(command, shell=True, stdout=PIPE).stdout
 output = json.load(stdout) 
 return output['posts'][stickied_posts]['post']



def identify(Post):
 img_url = Post['url']
 plant_id = requests.get(f'https://my-api.plantnet.org/v2/identify/all?api-key={PLANTNET_API_KEY}', {
        'images': [img_url],
        'organs': ['auto']
    }).json()

 table = ''
 for result in plant_id['results'][:5]:
  common_name = result['species']['commonNames'][0] if len(result['species']['commonNames']) != 0 else '/'
  scientific_name = result['species']['scientificNameWithoutAuthor']
  score = format(result['score'] * 100, '.2f')
  table += f'|{common_name}|{scientific_name}|{score} %|\\n'

 comment_text = f'''**Automatic identification via PlantNet summary**\\n\\n\\nMost likely match: **{plant_id['bestMatch']}**\\n\\n\\n|Common name|Scientific name|Likeliness|\\n|-|-|-|\\n{table}\\nBeep, boop\\n\\n\\nI am a bot, and this action was performed automatically.'''
 return comment_text


def createComment(postId, comment):
 command = '''curl -i -H \
 "Content-Type: application/json" \
 -X POST \
 -d '{
   "post_id": %s,
   "auth": "%s",
   "content": "%s"
 }' \
 https://mander.xyz/api/v3/comment ''' % (postId,LEMMY_JWT,comment)
 print(command)
 os.system(command)


#### Initialize ####

if 'old.txt' not in os.listdir(OLDID_FOLDER_PATH):
 with open(f'{OLDID_FOLDER_PATH}/old.txt','w') as oldId:
  oldPost = getNewestPost()
  oldId.write(str(oldPost['id']))

###########################


with open(f'{OLDID_FOLDER_PATH}/old.txt','r') as old:
 oldId = int(old.read())



newestPost = getNewestPost()
newestPostId = newestPost['id']
print(oldId)
print(newestPostId)

img_extensions = 'jpgpngjpegtiftiff'


with open(f'{OLDID_FOLDER_PATH}/old.txt','w') as old:
 old.write(str(newestPostId))

if (newestPostId != oldId) & ('url' in newestPost):
 img_url = newestPost['url']
 extension = img_url.split('.')[-1].lower()
 if extension in img_extensions:
  comment = identify(newestPost)
  createComment(newestPostId,comment) 
