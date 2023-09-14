import json
import math
import os
import socket


def floor(x):
    return int(math.floor(x))


def nroot(arr):
    return math.pow(arr[1], 1/arr[0])


def reverse(s):
    return s[::-1]


def validAnagram(strArr):
    s1 = strArr[0].replace(' ', '').lower()
    s2 = strArr[1].replace(' ', '').lower()
    hashmap1 = {}
    hashmap2 = {}

    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in hashmap1:
            hashmap1[i] = 1
        else:
            hashmap1[i] += 1
    for i in s2:
        if i not in hashmap2:
            hashmap2[i] = 1
        else:
            hashmap2[i] += 1
    return hashmap1 == hashmap2


def sort(strArr):
    return sorted(strArr)


def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serverAddress = '/socket_file'
    try:
        os.unlink(serverAddress)
    except FileNotFoundError:
        pass

    sock.bind(serverAddress)
    sock.listen(1)
    connection, _ = sock.accept()

    try:
        while True:
            print('--------------------')
            data = connection.recv(1024)
            print('received data : {}'.format(data.decode('utf-8')))
            receivedData = json.loads(data)
            method = receivedData['method']
            params = receivedData['params']
            paramTypes = receivedData['param_types']
            id = receivedData['id']
            funcHashmap = {
                'floor': floor,
                'nroot': nroot,
                'reverse': reverse,
                'validAnagram': validAnagram,
                'sort': sort
            }
            paramHash = {
                'floor': 'double',
                'nroot': '[int,int]',
                'reverse': 'string',
                'validAnagram': '[string,string]',
                'sort': 'string[]'
            }

            if method in funcHashmap:
                if str(paramTypes) != paramHash[method]:
                    sendData = 'Invalid parameter'
                else:
                    sendData = json.dumps({
                        'results': str(funcHashmap[method](params)),
                        'result_type': str(type(paramHash[method])),
                        'id': id
                    })
            else:
                sendData = 'Function not found'

            connection.sendall(sendData.encode('utf-8'))
            print('sent data : {}'.format(sendData))
    finally:
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    main()
