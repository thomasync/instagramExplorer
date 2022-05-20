# SEARCH.PY

Get facebook_places_id and pk by string

REQUEST
{
    'search_surface': 'places_serp',
    'timezone_offset': '7200',
    'count': '30',
    'query': 'montpellier',
}

RESPONSE (object -> items[])
	facebook_places_id
	pk
	address
	lat
	lng
	name
	short_name

-------------------------------------------------------------------

# MAP_REGION_GEOHUB.PY

Get stories from latitude coords

		. . . . T LAT . . . .
		. . . . . . . . . . .
		. . . . C LAT . . . .
		L LNG . . . . . R LNG
		. . . . C LNG . . . .
		. . . . . . . . . . .
		. . . . B LAT . . . .

REQUEST
{
   "bottom_lat":"43.18984606162919",
   "right_lng":"3.349006175994873",
   "top_lat":"43.5237292697286",
   "_uid":"1559749708",
   "_uuid":"0b5d6636-8663-439f-9e18-794cc5fe6ada",
   "center_lat":"43.35702120980384",
   "center_lng":"3.2198524475097656",
   "left_lng":"3.090698719024658"
}

RESPONSE
	geohub
		facebook_places_id
		pk
		lat
		lng
		name

-------------------------------------------------------------------

# STORIES.PY

Get stories from a pk id

REQUEST
{
   "exclude_media_ids":"[]",
   "supported_capabilities_new":"[{\"name\":\"SUPPORTED_SDK_VERSIONS\",\"value\":\"118.0,119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0,127.0,128.0,129.0,130.0,131.0,132.0,133.0,134.0,135.0,136.0\"},{\"name\":\"FACE_TRACKER_VERSION\",\"value\":\"14\"},{\"name\":\"segmentation\",\"value\":\"segmentation_enabled\"},{\"name\":\"COMPRESSION\",\"value\":\"ETC2_COMPRESSION\"},{\"name\":\"world_tracker\",\"value\":\"world_tracker_enabled\"},{\"name\":\"gyroscope\",\"value\":\"gyroscope_enabled\"}]",
   "source":"discovery_map_location_detail",
   "batch_size":"1",
   "_uid":"1559749708", (Ig-Intended-User-Id)
   "_uuid":"0b5d6636-8663-439f-9e18-794cc5fe6ada",
   "reel_ids":[
      "location:213110517:1651161986152" (pk : timestamp)
   ]
}


RESPONSE (reels -> location:(id) -> items[])
	id
	commerciality_status
	device_timestamp
	is_paid_partnership
	location
		facebook_places_id
		pk
		name
		address
		city
		lat
		lng
	media_type
	video_versions[0]
		url
	image_versions2
		candidates[0]
			url
	user
		full_name
		username
		profile_pic_url

-------------------------------------------------------------------

# LOCATION_STORIES.PY (/!\ NOT THE BEST)

Get stories from array of pk id

REQUEST
{
   "location_ids":"[326306567911656,125760108287186,154848494549951,1020385597,240120964,852381321591148,417779701722666,697377134,221532267895034,156181234804331,326884026,104201094344114,273273883,715392073,1029376249,347092666,1028087705,268910047,1034732460,396878023,509332785,1745965365664708,372259975,381981514,354048898610686,240897610,974227299358596]",
   "_uid":"1559749708",
   "_uuid":"0b5d6636-8663-439f-9e18-794cc5fe6ada"
}