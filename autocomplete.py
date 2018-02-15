import requests



def autocomplete(query):
	ENDPOINTS = ['https://www.google.com/complete/search', 'http://suggestqueries.google.com/complete/search']
	ENDPOINT = ENDPOINTS[0]

	payload = {'client': 'firefox', 'q': query}
	response = requests.get(ENDPOINT, params=payload)
	return response.json()[1]


def main():
	query = input('[*] Enter query: ')
	print('[*] Autocomplete results: {}'.format(autocomplete(query)))


if __name__=='__main__':
	main()
