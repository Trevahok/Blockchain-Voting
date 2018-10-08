import hashlib, json 
from time import time
class Blockchain():
    def __init__(self, *args, **kwargs):
        self.chain = []
        self.current_transacitons= []

        #genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof , previous_hash=None):
        block ={
            'index': len(self.chain) + 1 ,
            'timestamp' : time(), 
            'transactions': self.current_transacitons,
            'proof' : proof, 
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        pass
    def new_transaction(self, sender , recipient , amount):
        self.current_transaciton.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )
        return self.last_block['index']+1
    @staticmethod
    def hash(block):
        pass
    @property
    def last_block(self):
        return self.chain[-1] 