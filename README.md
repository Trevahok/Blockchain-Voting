# Blockchain Election Voting
An election voting system powered by the Blockchain technology. 

## Features:
- W3 Parallax Template
- Flask backend
- Custom Blockchain server

## Instructions to run:

- Run the Authentication service : runs on 5000 port
```python 
  python3 verifier.py
```
- Run the blockchain node:  runs on a random port between 5000 and 5009
```python
  python3 blockchain.py
```
- Change the port in the client.py to the port on which the blockchain is running.
- Run the client interface server:  runs on port 5010
```bash
  python3 client.py
```
- Access the server interface on localhost with the same port on which the blockchain node is running: 
  - For example , if the server is running on the port 5001
```
  In browser , open 127.0.0.1:5001
```
