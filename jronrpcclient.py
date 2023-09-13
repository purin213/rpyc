from jsonrpclib import Server


def main():
    conn = Server('http://localhost:8080')
    print(conn.findlen(('a', 'x', 'd', 'z'), 11, {'Mt. Abu': 1602, 'Mt. Nanda': 3001, 'Mt. Kirubu': 102, 'Mt.Nish': 5710}))


if __name__ == '__main__':
    main()
