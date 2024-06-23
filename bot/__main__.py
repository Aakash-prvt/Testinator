from bot import TelegramBot, logger
from aiohttp import web
import os
import asyncio

async def handle(request):
    return web.Response(text="Hello, Render!")

async def init_web_app():
    app = web.Application()
    app.router.add_get('/', handle)
    port = int(os.environ.get('PORT', 5000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def run_telegram_bot():
    logger.info('Initializing...')
    await TelegramBot.start()  # Use a method that doesn't start a new event loop
    await TelegramBot.idle()   # Keep the bot running

async def main():
    await asyncio.gather(
        init_web_app(),
        run_telegram_bot()
    )

if __name__ == '__main__':
    asyncio.run(main())
