import aiohttp
from config import API_URL, API_KEY

async def get_balance():
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, data={
            "key": API_KEY,
            "action": "balance"
        }) as response:
            return await response.json()

async def get_services():
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, data={
            "key": API_KEY,
            "action": "services"
        }) as response:
            return await response.json()
