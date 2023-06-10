from fastapi import FastAPI, Request,status
from fastapi.responses import RedirectResponse
from pyrogram import Client


app = FastAPI()


async def get_session(api_id, api_hash, bot_token):
    bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)
    await bot.start()  # Start the Pyrogram client
    session = await bot.export_session_string()
    await bot.stop()  # Stop the Pyrogram client after exporting the session
    return session


@app.get("/")
async def root():
    return RedirectResponse(url="https://github.com/iseshu/session-api/", status_code=status.HTTP_302_FOUND)


@app.get('/token')
async def token(request: Request):
    api_id = request.query_params.get('api_id')
    api_hash = request.query_params.get('api_hash')
    bot_token = request.query_params.get('bot_token')
    session = await get_session(int(api_id), api_hash, bot_token)
    return {"session": session,"api_id": api_id,"api_hash": api_hash,"bot_token": bot_token}
