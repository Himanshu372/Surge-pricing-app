from django.test import TestCase
from app.models import cabData
from django.utils import timezone
from django.urls import reverse_lazy, reverse, include, path, resolve
from model_mommy import mommy
from django.contrib import admin
from . import views


# Create your tests here.

# Test class for models
class cabDataTest(TestCase):


    # def create_cabData(self, user_id = '12345'):
    #                    # ,
    #                    # vehicle_model_id = 'abdc', package_id = None,
    #                    # travel_type_id = None, from_area_id = '3',
    #                    # to_area_id = '12', from_city_id = None, to_city_id = None,
    #                    # from_date = '01/01/2013  2:00:00 AM', to_date = '01/01/2013  4:00:00 AM',
    #                    # online_booking = None, mobile_site_booking = None, booking_created = None,
    #                    # from_lat = None, from_long = None, to_lat = None, to_long = None, car_cancellation = None):
    #     '''
    #
    #     :return:
    #     '''
    #     return cabData.objects.create(user_id = user_id)
    #                                   # ,
    #                                   # vehicle_model_id = vehicle_model_id,
    #                                   # package_id = package_id, travel_type_id = travel_type_id,
    #                                   # from_area_id = from_area_id, to_area_id = to_area_id, from_city_id = from_city_id,
    #                                   # to_city_id = to_city_id, from_date = from_date, to_date = to_date,
    #                                   # online_booking = online_booking, mobile_site_booking = mobile_site_booking,
    #                                   # booking_created = booking_created, from_lat = from_lat, from_long = from_long,
    #                                   # to_lat = to_lat, to_long = to_long, car_cancellation = car_cancellation)


    def test_cabdata_creation(self):
        cabData_obj = mommy.make(cabData)
        self.assertTrue(isinstance(cabData_obj, cabData))
        self.assertEqual(cabData_obj.__str__(), 'Trip was taken from area_id {} to area_id {} on {}'.format(cabData_obj.from_area_id, cabData_obj.to_area_id, cabData_obj.from_date))



class API_test(TestCase):
    urlpatterns = [
        path('', views.home),
        path('', include('app.urls')),
        path('admin/', admin.site.urls),
    ]
    def test_index_page(self):
        url = resolve('')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)












