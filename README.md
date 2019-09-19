# KAD
Experiments with Kademlia DHT over UDP using:
https://github.com/bmuller/kademlia/tree/master/kademlia

### DHT is controlled with ipython interactive shell embedded int app

### To start app run
```
python kad.py -p <UDP_PORT>
```
After entering an interacive shell use k object to:
* k.boot_to(host, port) - to boot network pointing one node
* k.set(key, value) - store key, value
* k.get(key, value) - retrieve value by key

for example

```
In [10]: k.boot_to('127.0.0.1',4444)
...
In [11]: k.set('key,'value')
...
In [12]: k.get('key')
...
```
