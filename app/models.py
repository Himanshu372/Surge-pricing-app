from django.db import models

# Create your models here.

from django.db import models

# Model for storing data from file
class cabData(models.Model):
    id = models.IntegerField(primary_key = True)
    user_id = models.CharField(max_length = 50, null=False)
    vehicle_model_id = models.CharField(max_length = 50, null = True)
    package_id = models.CharField(max_length=50, null=True)
    travel_type_id = models.CharField(max_length=50, null=True)
    from_area_id = models.CharField(max_length=50, null=True)
    to_area_id = models.CharField(max_length=50, null=True)
    from_city_id = models.CharField(max_length=50, null=True)
    to_city_id = models.CharField(max_length=50, null=True)
    from_date = models.CharField(max_length=50, null=True)
    to_date = models.CharField(max_length=50, null=True)
    online_booking = models.IntegerField(null = True)
    mobile_site_booking = models.IntegerField(null=True)
    booking_created =  models.CharField(max_length=50, null=True)
    from_lat = models.CharField(max_length=50, null=True)
    from_long = models.CharField(max_length=50, null=True)
    to_lat = models.CharField(max_length=50, null=True)
    to_long = models.CharField(max_length=50, null=True)
    car_cancellation = models.IntegerField(null=True)



    def __str__(self):
        return 'Trip was taken from area_id {} to area_id {} on {}'.format(self.from_area_id, self.to_area_id, self.from_date)