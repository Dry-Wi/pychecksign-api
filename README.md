# pychecksign
Simple python backend to validate signed message on front end

## Installation
To install run `poetry install` in the project folder

In order for the virtual env to be created in the project folder run `poetry config virtualenvs.in-project = true`

## Description
This api (using fastapi) verify that a message signed with a wallet is indeed signed by the address sent.
This mechanism can be used to register users as an alternative to the web2 approach (email / password). 
1. The server generates a nonce and sent it to the client to sign it
2  The client sign the message and send it back to the server with the public address
3. The server validate that the signature is indeed produced by the correct address signing the nonce sent
