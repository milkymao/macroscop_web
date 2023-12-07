import requests
import json

class Macroscop:
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
    def get_faces(self, faces=[]):
        with requests.session() as s:
            response = s.get(url=Macroscop.get_url(self),
                             auth=(self.headers['login_username'], self.headers['login_password']))
            for face in json.loads(response.text)['faces']:
                faces.append(face)
        return faces
    def get_data(self, i=0, data=[]):
        with requests.session() as s:
            faces = Macroscop.get_faces(self)
            for face in faces:
                face_id = f"{face['id']}"
                response = s.get(url=Macroscop.get_url(self, id=f'/{face_id}'),
                                 auth=(self.headers['login_username'], self.headers['login_password']))
                faces[i]["face_images"] = json.loads(response.text)['face_images']
                data.append(list(face.values())[:(-1)])
                data[i].append('/n'.join(list(face.values())[-1]))
                i += 1
        return data

# if __name__ == "__main__":
#     db = DataBase(host='localhost:8080')
#     print(db.get_data())