from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from app.models import cabData
from app.serializers import cabDataSerializer
import pandas as pd
import openpyxl
from itertools import islice
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request, 'app/index.html')



class surgePricingList(viewsets.ModelViewSet):
    queryset = cabData.objects.all()
    serializer_class = cabDataSerializer
    parser_classes = (FileUploadParser,)
    template_name = 'app/surge_price_page.html'

    @csrf_exempt
    def put(self, request, filename = 'my_file', format = None):
        '''

        :param request:
        :param filename:
        :param format:
        :return:
        '''
        SUPPORTED_FORMATS = ['.xlsx']
        print('Inside PUT')
        file_obj = request.data['file']
        print(file_obj)
        excel_file = openpyxl.load_workbook(file_obj)['data']
        data = excel_file.values
        cols = next(data)[0:]
        data = list(data)
        # idx = [r[0] for r in data]
        data = (islice(r, 0, None) for r in data)
        df = pd.DataFrame(data, columns=cols)
        for index, row in df.iterrows():
            d = cabData(id = row['id'], user_id = row['user_id'], vehicle_model_id = row['vehicle_model_id'], package_id = row['package_id'],
                        travel_type_id = row['travel_type_id'], from_area_id = row['from_area_id'], to_area_id = row['to_area_id'],
                        from_city_id = row['from_city_id'], to_city_id = row['from_city_id'], from_date = row['from_date'], to_date = row['to_date'],
                        online_booking = row['online_booking'], mobile_site_booking = row['mobile_site_booking'],
                        booking_created = row['booking_created'],from_lat = row['from_lat'],
                        from_long = row['from_long'], to_lat = row['to_lat'], to_long = row['to_long'],
                        car_cancellation = row['Car_Cancellation'])
            if self.queryset.filter(id = row['id']).exists():
                pass
            else:
                d.save()

        l = df['from_area_id'].groupby(by=df['from_date'].dt.hour).value_counts()

        k = l.reset_index(level=0, inplace=False)
        k['area'] = k.index.values
        k.columns = ['hour', 'counts', 'area']
        k.reset_index(level=0, inplace=True)
        k = k.drop(['from_area_id'], inplace=False, axis=1)

        bin_width = 200
        threshold = k['counts'].max() - bin_width

        k['surge'] = k.apply(lambda x: 0 if x['counts'] < threshold else (
            2 if x['counts'] == threshold + bin_width else (1 + ((x['counts'] % threshold) / (bin_width // 10)) * .1)),
                             axis=1)

        surge_dict = {i: {} for i in set(i for i in k.loc[k['counts'] > threshold, 'area'].values)}
        for i in k.loc[k['counts'] > threshold, ['hour', 'area', 'surge']].values:
            surge_dict[i[1]][i[0]] = round(i[2], 2)

        chart_dict = {}
        chart_dict['type'] = 'line'
        chart_dict['data'] = {}
        chart_dict['data']['labels'] = [i for i in range(25)]
        chart_dict['data']['datasets'] = []
        count = 0
        for i in set(i for i in k.loc[k['counts'] > threshold, 'area'].values):
            chart_dict['data']['datasets'].append({})
            chart_dict['data']['datasets'][count]['label'] = i
            chart_dict['data']['datasets'][count]['data'] = [1 if j not in surge_dict[i].keys() else surge_dict[i][j] for j in range(25)]
            chart_dict['data']['datasets'][count]['borderColor'] = '#3e95cd'
            chart_dict['fill'] = False
            count += 1
        chart_dict['data']['options'] = {}
        chart_dict['data']['options']['title'] = {}
        chart_dict['data']['options']['title']['display'] = True
        chart_dict['data']['options']['title']['text'] = 'Surge Rate by Area'

        return Response(chart_dict, status = 200)


    def list(self, request, *args, **kwargs):
        return render(request, template_name = self.template_name)






