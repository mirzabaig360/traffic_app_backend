from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import SensorData


class TrafficAPITestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        SensorData.objects.create(sensor_id=1, sensor_name="Sensor 1", mon_avg_count=200, tue_avg_count=167,
                                  wed_avg_count=548, thu_avg_count=456, fri_avg_count=74, sat_avg_count=85,
                                  sun_avg_count=96, date="2023-08-02")

        SensorData.objects.create(sensor_id=2, sensor_name="Sensor 2", mon_avg_count=210, tue_avg_count=137,
                                  wed_avg_count=57, thu_avg_count=155, fri_avg_count=14, sat_avg_count=13,
                                  sun_avg_count=653, date="2023-08-03")

    def test_get_day_of_week_average_count(self):
        # Get the URL for the 'day_of_week_average_count' API endpoint
        url = reverse('day_of_week_average_count')

        # Prepare the request data with start_date and end_date
        data = {'start_date': '2023-08-02', 'end_date': '2023-08-03'}

        # Send a GET request to the API endpoint with the provided data
        response = self.client.get(url, data)

        # Check that the response status code is 200 (HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the number of results in the response data
        self.assertEqual(len(response.data['results']), 2)

        # Check the response data for each sensor
        sensor1_data = response.data['results'][0]
        self.assertEqual(sensor1_data['sensor_id'], 1)
        self.assertEqual(sensor1_data['sensor_name'], 'Sensor 1')
        self.assertEqual(sensor1_data['mon_avg_count'], 200)
        self.assertEqual(sensor1_data['tue_avg_count'], 167)
        self.assertEqual(sensor1_data['wed_avg_count'], 548)
        self.assertEqual(sensor1_data['thu_avg_count'], 456)
        self.assertEqual(sensor1_data['fri_avg_count'], 74)
        self.assertEqual(sensor1_data['sat_avg_count'], 85)
        self.assertEqual(sensor1_data['sun_avg_count'], 96)

    def test_get_day_of_week_average_count_page_1(self):
        # Get the URL for the 'day_of_week_average_count' API endpoint
        url = reverse('day_of_week_average_count')

        # Prepare the request data with start_date, end_date and page
        data = {'start_date': '2023-08-02', 'end_date': '2023-08-03', 'page': 1}

        # Send a GET request to the API endpoint with the provided data
        response = self.client.get(url, data)

        # Check that the response status code is 200 (HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the number of results in the response data
        self.assertEqual(len(response.data['results']), 2)

    def test_missing_start_date_and_end_date(self):
        # Get the URL for the 'day_of_week_average_count' API endpoint
        url = reverse('day_of_week_average_count')

        # Send a GET request to the API endpoint without providing start_date and end_date
        response = self.client.get(url)

        # Check that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('start_date', response.data['error'])
        self.assertIn('end_date', response.data['error'])
