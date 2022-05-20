import unittest
from instagramExplorer import InstagramExplorer


class TestSearch(unittest.TestCase):

    def test_search(self):
        places = InstagramExplorer.search("Montpellier")
        
        self.assertGreater(len(places), 0)
        
        self.assertTrue('facebook_places_id' in places[0])
        self.assertTrue('pk' in places[0])
        self.assertTrue('address' in places[0])
        self.assertTrue('lat' in places[0])
        self.assertTrue('lng' in places[0])
        self.assertTrue('name' in places[0])
        self.assertTrue('short_name' in places[0])

    def test_search_length(self):
        places = InstagramExplorer.search("Montpellier", 12)
        self.assertEqual(len(places), 12)

if __name__ == '__main__':
    unittest.main()