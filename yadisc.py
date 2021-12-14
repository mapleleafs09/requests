from pprint import pprint

import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # def get_files_list(self):
    #     files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, file_path):

        href = self._get_upload_link(disk_file_path=file_path.split("/")[-1]).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        _file_name = file_path.split("/")[-1]
        if response.status_code == 201:
            print(f"Файл {_file_name} успешно загружен")