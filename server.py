from email import message
import logging
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

logger = logging.getLogger(__name__)


class MessageVerification(BaseModel):
    nonce: str
    signature: str
    address: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/verify")
async def verify(signedMessage: MessageVerification):
    logger.info(f'Verifying signature for message {signedMessage.nonce}')
