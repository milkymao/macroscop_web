import requests
import json

class DataBase:
    def __init__(self, host='127.0.0.1', offset='0', portion='1000', module='light', onlymainsample=False,
                 filter='', headers={'login_username': 'root','login_password': '','Content-Type': 'application/json'}):
        self.host = host
        self.id = id
        self.offset = offset
        self.portion = portion
        self.module = module
        self.onlymainsample = onlymainsample
        self.filter = filter
        self.headers = headers
    def get_url(self, id=''):
        return (f'http://{self.host}/api/faces{id}?offset={self.offset}&portion={self.portion}'
                f'&module={self.module}&onlymainsample={self.onlymainsample}&filter={self.filter}')
    def get_faces(self):
        with requests.session() as s:
            response = s.get(url=DataBase.get_url(self),
                             auth=(self.headers['login_username'], self.headers['login_password']))
            js_string = json.loads(response.text)
            faces = []
            for face in js_string['faces']:
                faces.append(face)
            return faces
    def get_data(self, i=0, data=[]):
        with requests.session() as s:
            faces = DataBase.get_faces(self)
            for face in faces:
                face_id = f"{face['id']}"
                response = s.get(url=DataBase.get_url(self,id=f'/{face_id}'),
                                 auth=(self.headers['login_username'], self.headers['login_password']))
                js_string = json.loads(response.text)
                face_images = js_string['face_images']
                faces[i]["face_images"] = face_images
                data.append(list(face.values())[:(-1)])
                data[i].append('/n'.join(list(face.values())[-1]))
                i += 1
            return data

if __name__ == "__main__":
    r = DataBase(host='localhost:8080')
    # print(r.get_data())
    print(r.get_data())