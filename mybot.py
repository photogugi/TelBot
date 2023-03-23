from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
import instaloader


L = instaloader.Instaloader()

start_msg = 'THIS BOT IS STILL IN DEVELOPMENT'

bot = Client('Instagram_Helper_Bot', api_id='25125440', api_hash='e3ae7b480e752be85ece64007e900380', bot_token='6057598046:AAEBC05AGeaiB3PNDC3ZxZE3lVb3FAdEt_4')


#FOR /START MESSAGE
@bot.on_message(filters.command('start'))
def greet(bot, message):
	bot.send_message(message.chat.id, start_msg)
	
#TO DOWNLOAD ANY KIND OF PICTURE USE THIS....
@bot.on_message(filters.text)
def send_pic(bot, message):
	if 'https://www.instagram.com/reel/' in message.text:
		try:
			url = message.text
	
			metadata = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])._asdict()

	# Get the .mp4 file link
			mp4_url = metadata['video_url']

			bot.send_video(message.chat.id, mp4_url)
			
		except Exception as err:
			bot.send_message(message.chat.id, f'Sorry my bad!  I got the following error while performing the job \n \n -> {err}')
		
	elif 'https://www.instagram.com/p/' in message.text:
		try:
			url = message.text
			post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
			jpg_url = post.url
			bot.send_photo(message.chat.id, jpg_url)
		
		except Exception as err:
			bot.send_message(message.chat.id, f'Sorry my bad!  I got the following error while performing the job \n \n -> {err}')	
		
		

	


print('I AM ALIVE')
bot.run()