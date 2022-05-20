import unittest
from instagramExplorer import InstagramExplorer


class TestSearchFromLatitudes(unittest.TestCase):

    def test_retrieve_latitudes_from_center(self):
        latitudes = InstagramExplorer.retrieveLatitudesFromCenter(43.608783, 3.879928)

        self.assertEqual(latitudes['top_lat'], 44.075491059920004)
        self.assertEqual(latitudes['center_lat'], 43.608783)
        self.assertEqual(latitudes['bottom_lat'], 43.14207494008,)
        self.assertEqual(latitudes['left_lng'], 3.75077427152)
        self.assertEqual(latitudes['center_lng'], 3.879928)
        self.assertEqual(latitudes['right_lng'], 4.00908172848)

    def test_search_from_latitudes1(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                43.608783, 
                3.879928
            )
        )
        
        self.assertTrue('facebook_places_id' in place)
        self.assertTrue('pk' in place)
        self.assertTrue('lat' in place)
        self.assertTrue('lng' in place)
        self.assertTrue('name' in place)

        self.assertEqual(place['name'], 'Montpellier')
    
    def test_search_from_latitudes2(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                41.383539, 
                2.177600
            )
        )
        
        self.assertTrue('facebook_places_id' in place)
        self.assertTrue('pk' in place)
        self.assertTrue('lat' in place)
        self.assertTrue('lng' in place)
        self.assertTrue('name' in place)

        self.assertEqual(place['name'], 'Barcelone')

    def test_search_from_latitudes3(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                48.858278, 
                2.294619
            )
        )
        
        self.assertTrue('facebook_places_id' in place)
        self.assertTrue('pk' in place)
        self.assertTrue('lat' in place)
        self.assertTrue('lng' in place)
        self.assertTrue('name' in place)

        self.assertEqual(place['name'], 'Paris')

    def test_search_from_latitudes_distance1(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                48.858278, 
                2.294619,
                0
            )
        )

        self.assertEqual(place['name'], '7th arrondissement of Paris')
    
    def test_search_from_latitudes_distance2(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                48.858278, 
                2.294619,
                2
            )
        )

        self.assertEqual(place['name'], 'Ile-de-France, France')

    def test_search_from_latitudes_distance3(self):
        place = InstagramExplorer.searchFromLatitudes(
            InstagramExplorer.retrieveLatitudesFromCenter(
                48.858278, 
                2.294619,
                15
            )
        )

        self.assertEqual(place['name'], 'France')

if __name__ == '__main__':
    unittest.main()