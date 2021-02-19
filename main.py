from gpx_util import Gpx
import os


while True:
    print('[w] Write tranning\n[e] Exit')
    if input() == 'w' :
        print('\n\n')
        GPXFile_list = os.listdir('GPX_files')
        for number in range(len(GPXFile_list)):
            print(f'[{number}] {GPXFile_list[number]}')
        path_to_GPXFile = f"GPX_files/{GPXFile_list[int(input('Write number of file :  '))]}"
        type_of_tran =  input('Write tran type :  ')
        count_periods =  int(input('Write count periods :  '))
        periods_info = {}
        for period in range (1, count_periods+1):
            periods_info[period] = input(f'Write Time and HZone for {period} (Format: MM:SS,Z) :  ')


        gpx = Gpx(path_to_GPXFile, count_periods, periods_info, type_of_tran)
        print('\n\n_______RESULT_______')
        gpx.get_info()
        print('\n\n')
    else:
        break

