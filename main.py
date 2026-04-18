from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
```

Kodni ishlatish uchun misol:
```python
cache = LRUCache(2)  # 2 capacity

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)  # 2 is removed
print(cache.get(2))  # -1 (not found)
cache.put(4, 4)  # 1 is removed
print(cache.get(1))  # -1 (not found)
print(cache.get(3))  # 3
print(cache.get(4))  # 4
