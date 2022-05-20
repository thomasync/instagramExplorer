from math import dist
import os, json, requests
from html import escape
from datetime import datetime

class InstagramExplorer:
    
    """
        Get places informations from a location string
        
        Parameters:
            name (str) : Place
            count (int) : Number of results
            timezone_offset (int) : Offset for limiting results

        Returns:
            (
                facebook_places_id (int)
                pk (int)
                address (str)
                lat (float)
                lng (float)
                name (str)
                short_name (str)
            )[]
    """
    @staticmethod
    def search(name, count = 30, timezone_offset = 7200):
        places = []
        try:
            data = InstagramExplorer.__makeGetRequest("https://i.instagram.com/api/v1/fbsearch/places/", {
                'search_surface': 'places_serp',
                'timezone_offset': str(timezone_offset),
                'count': str(count),
                'query': name,
            })
            i = 0
            for item in data['items']:
                places.append({
                    'facebook_places_id': item['location']['facebook_places_id'],
                    'pk': item['location']['pk'],
                    'address': item['location']['address'],
                    'lat': item['location']['lat'],
                    'lng': item['location']['lng'],
                    'name': item['location']['name'],
                    'short_name': item['location']['short_name'],
                })
                i += 1
                if i >= count:
                    break
        except:
            pass
        
        return places
    
    """
        Get place from latitudes

        Parameters:
            Object or retrieveLatitudesFromCenter()

        Returns:
            (
                facebook_places_id (int)
                pk (int)
                lat (float)
                lng (float)
                name (str)
            ){}

    """
    @staticmethod
    def searchFromLatitudes(latitudes):
        place = {}
        try:
            response = InstagramExplorer.__makePostRequest('https://i.instagram.com/api/v1/map/map_region_geohub/', latitudes)
            place = {
                'facebook_places_id': response['geohub']['facebook_places_id'],
                'pk': response['geohub']['pk'],
                'lat': response['geohub']['lat'],
                'lng': response['geohub']['lng'],
                'name': response['geohub']['name']
            }
        except:
            pass

        return place

    """
        Retrieve multiples points of latitude/longitude from center
        
        . . . . T LAT . . . .
		. . . . . . . . . . .
		. . . . C LAT . . . .
		L LNG . . . . . R LNG
		. . . . C LNG . . . .
		. . . . . . . . . . .
		. . . . B LAT . . . .

        Parameters:
            latitude (float) 
            longitude (float)
            distance (float) : Distance from center in meters

        Returns:
            {}
    """
    @staticmethod
    def retrieveLatitudesFromCenter(latitude, longitude, distance = 1):
        return {
            'top_lat':      latitude + (0.46670805992 * distance),
            'center_lat':   latitude,
            'bottom_lat':   latitude - (0.46670805992 * distance),
            'left_lng':     longitude - (0.12915372848 * distance),
            'center_lng':   longitude,
            'right_lng':    longitude + (0.12915372848 * distance)
        }


    """
        Get stories from place id
    """
    def getStoriesFromPlace(id, excludeds = []):
        stories = {
            'items': [],
            'media_ids': []
        }
        try:
            response = InstagramExplorer.__makePostRequest('https://i.instagram.com/api/v1/feed/reels_media_stream/', {
                'exclude_media_ids': str(excludeds),
                'source':'discovery_map_location_detail',
                'reel_ids':[
                    'location:{}:{}'.format(id, datetime.timestamp(datetime.now()) - 3600)
                ]
            })
            response = response['reels'][list(response['reels'].keys())[0]]
            stories['media_ids'] = response['media_ids']

            for item in response['items']:
                if item['commerciality_status'] != "not_commercial" or item['is_paid_partnership'] == True:
                    continue

                infos = {
                    'id': item['id'],
                    'timestamp': item['device_timestamp'],
                    'type': item['media_type'],
                    'image': item['image_versions2']['candidates'][0]['url'],
                    'user': {
                        'name': item['user']['full_name'],
                        'username': item['user']['username'],
                        'image': item['user']['profile_pic_url']
                    },
                    'location': {
                        'facebook_places_id': item['location']['facebook_places_id'],
                        'pk': item['location']['pk'],
                        'name': item['location']['name'],
                        'address': item['location']['address'],
                        'city': item['location']['city'],
                        'lat': item['location']['lat'],
                        'lng': item['location']['lng']
                    } 
                }

                if infos['type'] == 2:
                    infos['video'] = item['video_versions'][0]['url']

                stories['items'].append(infos)

        except:
            pass

        return stories



    """
        Make a get request on the Instagram API
    """
    @staticmethod
    def __makeGetRequest(url, params={}):
        request = requests.get(url, params=params, headers=InstagramExplorer.__getHeaders())
        return json.loads(request.text)

    """
        Make a post request on the Instagram API
    """
    @staticmethod
    def __makePostRequest(url, data, params={}):
        data = 'signed_body=SIGNATURE.' + str(data).replace('{', '%7B').replace('}', '%7D').replace('[', '%5B').replace(']', '%5D').replace('\'', '%22').replace(':', '%3A')
        request = requests.post(url, data=data, headers=InstagramExplorer.__getHeaders())
        return json.loads(request.text)

    """
        Get headers for authentification
    """
    @staticmethod
    def __getHeaders():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "headers.json"), 'r') as headers:
            return json.loads(headers.read())