from influxdb import InfluxDBClient
from .config import DATABASE_NAME, DATABASE_HOST, DATABASE_PORT


class Influx:
	def __init__(self):
		self.cliend = InfluxDBClient(host=DATABASE_HOST, port=DATABASE_PORTc)
		self.cliend.switch_database(DATABASE_NAME)

	def add(self, filename, times, sadness, disgust, fear, enthusiasm, anger, happiness, neutral):
		if len(times) != len(sadness) != len(disgust) != len(fear) != len(enthusiasm) != len(anger) != len(happiness) != len(neutral):
			raise Except("Length of your data isn`t same!")
		points = []
		for i in times:
			data = {"measurement": filename,
					"time": times[i],
					"fields": {
							"sadness": sadness[i],
							"disgust": disgust[i],
							"fear": fear[i],
							"enthusiasm": enthusiasm[i],
							"anger": anger[i],
							"happiness": happiness[i],
							"neutral": neutral[i]
						}
					}
			points.append(data)
		self.cliend.write_points(points)
