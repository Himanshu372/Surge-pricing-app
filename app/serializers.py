from rest_framework import serializers
from app.models import cabData



class cabDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = cabData
        fields = ['id','user_id','vehicle_model_id','package_id','travel_type_id','from_area_id','to_area_id','from_city_id','to_city_id','from_date','to_date','online_booking','mobile_site_booking','booking_created','from_lat','from_long','to_lat','to_long','car_cancellation']




