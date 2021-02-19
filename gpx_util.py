from lxml import etree as et
import math
from datetime import datetime

class Gpx():
    def __init__(self, gpx_file, count_periods, periods_info, type_of_tran):
        self.parsed_file = et.parse(gpx_file)
        root = self.parsed_file.getroot()
        # Information
        self.date = root[0][-1].text
        # Data
        self.trk_list = list(root[1][1])
        self.count_periods = count_periods
        self.periods_info = periods_info
        self.type_of_tran = type_of_tran


    def __calculate_distance(self, start_lat_lon, end_lat_lon):
        R = 6371 # Radius of Earth in km

        start_lat = start_lat_lon['lat']
        start_lon = start_lat_lon['lon']
        end_lat = end_lat_lon['lat']
        end_lon = end_lat_lon['lon']

        dLat = math.radians(float(end_lat) - float(start_lat))
        dLon = math.radians(float(end_lon) - float(start_lon))
        lat1 = math.radians(float(start_lat))
        lat2 = math.radians(float(end_lat))

        a = math.sin(dLat/2) * math.sin(dLat/2) + \
            math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2) * math.sin(dLon/2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = R * c

        return d
    
    def __get_distance(self, loc_list):
        distance = 0
        for point_num in range(0,len(loc_list)-1):
            distance += self.__calculate_distance(loc_list[point_num], loc_list[point_num+1])
        return distance

    def __get_time(self, time_list):
        return datetime.strptime(time_list[-1], '%Y-%m-%dT%H:%M:%SZ') - datetime.strptime(time_list[0], '%Y-%m-%dT%H:%M:%SZ')

    def __get_HR(self, hr_list):
        return sum(hr_list)/len(hr_list)

    def get_info(self):
        periods_final  = {}
        for period in range(1, self.count_periods+1):
            periods_final[period] = {
                'loc_list':[],
                'time_list':[], 
                'hr_list':[], 
                'distance': 0, 
                'time' : '',
                'hr': '',
                'hrZone': 0
            }
            
            for item in self.trk_list:
                pass
                
        