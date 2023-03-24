from fastapi import FastAPI
import digitalocean

import os

app = FastAPI()
TOKEN = os.environ['TOKEN']
VPC_UUID = os.environ['VPC_UUID']

async def create_droplet():
    global TOKEN
    global VPC_UUID

    droplet = digitalocean.Droplet(
        token=TOKEN,
        name='minecraft-test-from-fastapi',
        size='s-1vcpu-2gb',
        region='nyc1',
        image='ubuntu-22-10-x64',
        monitoring=True,
        vpc_uuid=VPC_UUID,
        tags=['minecraft']
    )

    droplet.create()
    droplet.load()

    return droplet

@app.post('/create-server')
async def create_server():
    await create_droplet()

    return {}
