import unittest
from instagramExplorer import InstagramExplorer


class TestGetStories(unittest.TestCase):

    def test_get_stories(self):
        pkId = InstagramExplorer.search("Montpellier")[0]['pk']
        stories = InstagramExplorer.getStoriesFromPlace(pkId)
        
        self.assertGreater(len(stories['items']), 0)
        self.assertGreater(len(stories['media_ids']), 0)

        self.assertTrue('id' in stories['items'][0])
        self.assertTrue('timestamp' in stories['items'][0])
        self.assertTrue('type' in stories['items'][0])
        self.assertTrue('image' in stories['items'][0])
        
        self.assertTrue('user' in stories['items'][0])
        self.assertTrue('name' in stories['items'][0]['user'])
        self.assertTrue('username' in stories['items'][0]['user'])
        self.assertTrue('image' in stories['items'][0]['user'])

        self.assertTrue('location' in stories['items'][0])
        self.assertTrue('facebook_places_id' in stories['items'][0]['location'])
        self.assertTrue('pk' in stories['items'][0]['location'])
        self.assertTrue('name' in stories['items'][0]['location'])
        self.assertTrue('address' in stories['items'][0]['location'])
        self.assertTrue('city' in stories['items'][0]['location'])
        self.assertTrue('lat' in stories['items'][0]['location'])
        self.assertTrue('lng' in stories['items'][0]['location'])

        self.assertEqual(stories['items'][0]['location']['name'], "Montpellier")

if __name__ == '__main__':
    unittest.main()