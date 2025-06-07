import asyncio
from playwright.async_api import async_playwright
from models import TokenTask
from utils.logger import setup_logger

logger = setup_logger("token_solver")

CAPTCHA_SCRIPT = """
turnstile.render('#demo', {
    sitekey: '%s',
    callback: function(token) {
        window.__token__ = token;
    }
});
"""


async def solve_token(task: TokenTask):
    logger.info("Запуск playwright для URL: %s", task.website_url)
    logger.info("User-Agent: %s", task.user_agent)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=task.user_agent)
        page = await context.new_page()

        logger.info("Открытие страницы...")
        await page.goto(task.website_url, wait_until="domcontentloaded")

        logger.info("Ожидание появления встроенного токена...")
        token = None

        for _ in range(20):

            token = await page.evaluate("""
                () => {
                    const el = document.querySelector('input[name="cf-turnstile-response"]');
                    return el ? el.value : null;
                }
            """)
            if token:
                logger.info("✅ Токен найден в DOM: %s...", token[:30])
                break
            await asyncio.sleep(0.5)

        if not token:
            logger.warning("❌ Не удалось получить токен из DOM.")

        await browser.close()
        return {"token": token or ""}

