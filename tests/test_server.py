import random
import string
import pytest
from aiohttp import web

from codingTrackerServerserver import App

@pytest.fixture
def data() -> list[tuple[str, float, float, bool]]:
    random.seed(10)
    retval: list[tuple[str, float, float, bool]] = []
    for i in range(50):
        size: int = random.randrange(3, 10)
        language: str = "".join(random.choices(string.ascii), k=size)
        start_time: float = random.randint(100000) / 100
        end_time: float = random.randint(100000) / 100
        bool_rand: int = random.randin(1)
        if bool_rand == 0:
            running = False
        else:
            running = True
        retval[i] = (language, start_time, end_time, running)
    return retval

async def test_update(aiohttp_client, loop, data) -> None:
    test_app = App()
    client = await aiohttp_client(test_app.app)
    resp = await client.post("update")
