import csv, os, glob


def load_sensor_data():
    senor_data = []
    print(os.getcwd())
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                senor_data.append(row)
    return senor_data
