import requests

class redirector():

    def __init__(self, ws_ip):
        self.funcoes = {"adicionar" : "<post>/Tarefa",
                    "listar" : "<get>/Tarefa",
                    "buscar" : "<get>/Tarefa/<id>",
                    "apagar" : "<delete>/Tarefa/<id>",
                    "atualizar" : "<put>/Tarefa/<id>"}

        self.webserverIP = ws_ip

    def redirect_request(self, request, params=None):

        endpoint = self.funcoes[request]

        if "<id>" not in endpoint:

            if "<post>" in endpoint:
                endpoint = endpoint.replace("<post>", self.webserverIP)
                # payload = {'atributo1' : '%s' % params[2], 'atributo2' : '%s' % params[3]}
                response = requests.post(endpoint, data=params)

                if response.status_code == 200:
                    return (response.text)
                elif response.status_code == 404:
                    return (404)

            elif "<get>" in endpoint:
                endpoint = endpoint.replace("<get>", self.webserverIP)
                response = requests.get(endpoint)

                if response.status_code == 200:
                    return (response.text)
                elif response.status_code == 404:
                    return (404)

        else:

            endpoint = endpoint.replace("<id>", str(params[0]))

            if "<put>" in endpoint:
                endpoint = endpoint.replace("<put>", self.webserverIP)
                # payload = {'atributo1' : '%s' % params[1], 'atributo2' : '%s' % params[2]}
                response = requests.put(endpoint, data=params[1])

                if response.status_code == 200:
                    return (response.text)
                elif response.status_code == 404:
                    return (404)

            elif "<delete>" in endpoint:
                endpoint = endpoint.replace("<delete>", self.webserverIP)
                response = requests.delete(endpoint)

                if response.status_code == 200:
                    return (response.text)
                elif response.status_code == 404:
                    return (404)

            elif "<get>" in endpoint:
                endpoint = endpoint.replace("<get>", self.webserverIP)
                response = requests.get(endpoint)

                if response.status_code == 200:
                    return (response.text)
                elif response.status_code == 404:
                    return (404)

class globaldict():

    def __init__(self):
        self.dict = {}
        self.last_id = 0

    def add_coisa(self, coisa):
        self.dict[self.last_id] = coisa
        self.last_id += 1

    def get_coisa(self, id):
        if (int(id) < self.last_id):
            return self.dict[int(id)]
        else:
            return False

    def update_coisa(self, id, coisa):
        if (int(id) < self.last_id):
            self.dict[int(id)] = coisa
            return True
        else:
            return False


    def deleta_coisa(self, id):
        if (int(id) < self.last_id):
            del self.dict[int(id)]
        else:
            return False

class Tarefas():

    def __init__(self):
        attr1 = 0
        attr2 = 0
