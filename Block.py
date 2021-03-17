import hashlib
import json


class Block(object):
    def __init__(self, index: int, timestamp, data, previous_hash=''):
        self._index = index
        self._timestamp = timestamp.strftime(format='%A %d/%m/%Y %H:%M:%S')
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash for the current Block.
        :return: str
        """
        self_serialized_object = {
            'index': self._index,
            'timestamp': self._timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }
        self_object_encoded = json.dumps(self_serialized_object).encode()
        return hashlib.sha256(self_object_encoded).hexdigest()

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True)
