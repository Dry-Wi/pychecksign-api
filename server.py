import logging
from pydantic import BaseModel
from eth_account import Account
from eth_account.messages import encode_defunct
from web3.auto import w3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    recovered_address = (w3.eth.account.recover_message(
        message, signature=signature))

    result = {
        'signer_address': signed_message.address,
        'verify_result': (recovered_address == signed_message.address),
        'recovered_address': recovered_address
    }

    logging.debug(result)

    return result
