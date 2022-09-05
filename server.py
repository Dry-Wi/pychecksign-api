from email import message
import logging
from pydantic import BaseModel
from fastapi import FastAPI
from eth_account.messages import encode_defunct
from web3.auto import w3

app = FastAPI()
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MessageVerification(BaseModel):
    nonce: str
    signature: str
    address: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/verify")
async def verify(signed_message: MessageVerification):
    logger.info(f'Verifying signature for message: {signed_message.nonce}')

    # Getting user's signature from the request body
    signature = signed_message.signature

    # We verify the signature with the original message
    message = encode_defunct(text=signed_message.nonce)
    signed_address = (w3.eth.account.recover_message(
        message, signature=signature)).lower()

    return {
        'verify_result': (signed_address == signed_message.signature)
    }
