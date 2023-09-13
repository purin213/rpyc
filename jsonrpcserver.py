from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def findlen(*args):
    res = []
    for arg in args:
        try:
            lenval = len(arg)
        except TypeError:
            lenval = None
        res.append((lenval, arg))
    return res


def main():
    server = SimpleJSONRPCServer(('localhost', 8080))
    server.register_function(findlen)
    print("Starting server")
    server.serve_forever()


if __name__ == '__main__':
    main()
