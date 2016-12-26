import os

class AzFuncHTTPReq:
    def __init__(self, binding_name=None):
        self._headers = {}
        self._method = os.environ['REQ_METHOD'].lower()
        self._query = {}
        self._body = ""

        for var in os.environ:
            if var[:12] == 'REQ_HEADERS_':
                self._headers[var[12:].lower()] = os.environ[var].lower()
            elif var[:10] == 'REQ_QUERY_':
                self._query[var[10:].lower()] = os.environ[var].lower()
            else:
                print("{} = {}".format(var, os.environ[var]))

        with open(binding_name, mode='r') as body:
            self._body = body.read()

    @property
    def headers(self):
        return self._headers

    @property
    def query(self):
        return self._query

    @property
    def method(self):
        return self._method

    @property
    def body(self):
        return self._body


def main():
    request = AzFuncHTTPReq(binding_name='req')
    for header in request.headers:
        print('{} = {}'.format(header, request.headers[header]))

if __name__ == "__main__":
    main()