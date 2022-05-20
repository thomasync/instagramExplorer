from instagramExplorer import InstagramExplorer


#from instagramExplorer import InstagramExplorer

#pk = 225392975

#latitudes = Instagram.retrieveLatitudesFromCenter(43.35702120980384, 3.2198524475097656, 10)
#locations = Instagram.searchFromLatitudes(latitudes)

stories = InstagramExplorer.getStoriesFromPlace(225392975)
for story in stories['items']:
    print(story['user']['username'])
