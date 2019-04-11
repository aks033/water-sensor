import requests
import datetime
import ast 
import dateutil.parser

def write_to_file(data,f):
	for i in data:
			f.write(str(dateutil.parser.parse(i["time"]))+ ","+ str(i["volume"]) + "\n")




def main():

	headers = {
	"Content-Type" : "application/json",
	"Authorization" : "Bearer xPAOImRDeggl1KBLunUyNyPqeD_4cX61mZ9vqygnHISOa2qRc7h-Cg"
	}
	url = 'https://api.streamlabswater.com/v1/locations'
	req = requests.get(url, headers=headers)
	print req.text

	total_pages = 0
	# locationId = "6632885f-31d6-4594-8bf1-cdb609e05096"
	# filename = "waterdata.csv"
	locationId = "03d367d4-00a6-4f7c-b3d5-1f3a5db2b186" # hot water
	filename = "hotwater.csv"
	startTime =  '2018-02-01T00:00:00.00Z'



	# get number of pages
	url = 'https://api.streamlabswater.com/v1/locations/{}/readings/water-usage?startTime={}&page=0'.format(locationId,startTime) 
	req = requests.get(url, headers=headers)
	# print type(req.text)
	total_pages = ast.literal_eval(req.text)["pageCount"]

	# file desc
	f= open(filename,"w")

	for page in xrange(1,total_pages + 1):

		url = 'https://api.streamlabswater.com/v1/locations/{}/readings/water-usage?startTime={}&page={}'.format(locationId,startTime,page) 
		req = requests.get(url, headers=headers)
		data = ast.literal_eval(req.text)
		# print data
		write_to_file(data["readings"] , f)


	f.close()


if __name__ == '__main__':
	main()
