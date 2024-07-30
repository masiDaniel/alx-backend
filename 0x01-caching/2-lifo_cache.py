#!usr/bin/env python3
"""
Defines a class LIFOCache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    last_accessed = None  # stores last accesed key

    def __init__(self):
        """
        Intantiates values
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value for the key in the
        dictionary self.cache_data
        """
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) == self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                self.last_accessed = list(self.cache_data)[-1]
                self.cache_data[key] = item
                if len(self.cache_data) > self.MAX_ITEMS:
                    self.cache_data.pop(self.last_accessed)
                    print(f"DISCARD: {self.last_accessed}")
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data
        linked to key
        """
        if key is None:
            return None
        gotten_key = self.cache_data.get(key)
        if gotten_key is None:
            return None
        return gotten_key
