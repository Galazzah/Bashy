import requests

def get_response(url: str) -> dict:
	response = requests.get(URL)
	return response.json()['result']

def get_package(pckg_json: dict, pckg_name: str) -> dict:
	for package in pckg_json:
		if package['Name'] == pckg_name:
			return package

#install package flow
def get_package_url(pckg_name: str) -> str:
	pckg = get_package(pckg_name)
	return pckg['URL']

#update package flow
def get_version(pckg_json: dict, pckg_name: str) -> float:
	pckg = get_package(pckg_name)
	return pckg['Version']




