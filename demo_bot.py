import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "lgrant146", oauth_token=os.getenv("GH_AUTH"))

        await gh.post('/repos/lgrant146/stage1bot/issues',
                      data={
                          'title': 'Test',
                          'body': 'We can post issues',
                      })


asyncio.run(main())
