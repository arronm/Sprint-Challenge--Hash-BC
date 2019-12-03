import os
import requests
from multiprocessing import Process, Manager
from uuid import uuid4
import json
import hashlib

from miner_t import mine_t
from miner_s import mine_s

class MineController():
    def __init__(self, miners, shared, node="http://localhost:5000"):
        self.shared = shared
        self.miners = miners
        self.node = node
        self.get_id()
        self.shared['restart'] = uuid4()

    def get_id(self):
        if os.path.exists("my_id"):
            id_file = open("my_id", "r+")
            my_id = id_file.read()
        else:
            id_file = open("my_id", "w+")
            my_id = str(uuid4()).replace('-', '')
            id_file.write(my_id)
        self.id = my_id

    def send_proof(self, proof, miner):
        proofData = {
            'proof': proof,
            'id': self.id
        }
        response = requests.post(f'{self.node}/mine', json=proofData)
        if json.loads(response.content)['message'] is None:
            print(f'{miner} mined successfully')
        else:
            print(json.loads(response.content)['message'])
        self.shared['restart'] = uuid4()

    def validate_proof(self, last_hash, proof):
        guess = f'{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:6] == last_hash[-6:]

    def add_one(self, proof):
        return proof + 1

    def find_proof(self, mod=add_one):
        response = requests.get(url=self.node + "/last_proof")
        last_proof = response.json().get('proof')
        last_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()
        proof = 0
        restart = self.shared['restart']
        while self.validate_proof(last_hash, proof) is False:
            if restart != self.shared['restart']:
                print('restarting')
                return None
            proof = mod(proof)

        return proof

    def mine(self):
        processes = []

        for miner in self.miners:
            process = Process(
                target=miner,
                args=(self.find_proof, self.send_proof)
            )
            processes.append(process)

        for process in processes:
            process.start()
            process.join()


if __name__ == "__main__":
    manager = Manager()
    shared = manager.dict()
    mc = MineController([mine_t, mine_s], shared, node="https://lambda-coin.herokuapp.com/api")
    mc.mine()
