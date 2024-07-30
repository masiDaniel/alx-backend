#!usr/bin/env python3
"""
Defines a class MRUCache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    keys = []

    def put(self, key, item):
        """
        Assigns the item value for the key in the
        dictionary self.cache_data
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            first_item = self.keys.pop(-2)
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}")

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
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        return gotten_key
