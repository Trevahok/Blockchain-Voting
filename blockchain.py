import hashlib, json 
from textwrap import dedent
from uuid import uuid4
from flask import Flask 
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
        self.current_transacitons=[]
        self.chain.append(block)

        return block
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
        block_string = json.dumps(block , sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1] 
    def proof_of_work(self , last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof+=1
        return proof
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4]== '0000'



app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods= ['GET'])
def mine():
    return 'bitch money here'
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return ' new shit here'
@app.route('/chain' , methods=['GET'])
def full_chain():
    response={
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return json.dumps(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)