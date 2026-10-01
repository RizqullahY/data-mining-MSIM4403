# Z-Score Normalization
import numpy
import statistics

fitur_1 = [4 , 2 , 7 , 3 , 9 , 6]
fitur_2 = [8 , 3 , 2 , 7 , 6 , 9]


# print(statistics.mean(fitur_1))

def tugas_tutorial(data_list):
    print()
    print('=' * 20)
    mean = statistics.mean(data_list)
    print(f'RATA RATA : {mean:.3f}')

    simpangan_baku = numpy.std(data_list)
    print()
    print(f'SIMPANGAN BAKUNYA : {simpangan_baku:.3f}')
    print()

    for i in data_list:
        z = ( i - mean ) / simpangan_baku
        print(f'( {i} - {mean:.3f} ) / {simpangan_baku:.3f} = {z:.3f}')

tugas_tutorial(fitur_1)
tugas_tutorial(fitur_2)
