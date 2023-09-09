from aiohttp import web
import json

from config import Config
from codingTrackerServer.persistence import Persistence


class App:
    def __init__(self, db: str = "./data/database.db"):
        self.app: web.Application = web.Application()
        self.persistence: Persistence = Persistence(file_path=db)
        self._init_config()
        self._init_routes()

    def run(self) -> None:
        web.run_app(self.app)

    def _init_routes(self) -> None:
        self.app.add_routes([web.post("/update", self._update)])
        self.app.add_routes([web.post("/languages", self._languages)])

    def _init_config(self) -> None:
        cfg = Config()
        self.app["config"] = cfg.config()

    def _update(self, request) -> None:
        bcontent: bytes = request.read()
        content: list[tuple[str, float, float, bool]] = json.loads(bcontent)
        try:
            self.persistence.update(content)
        except ValueError:
            return web.Response(status=404)
        print(content)
        return web.Response(status=200)

    def _languages(self, request) -> None:
        tallies: dict[str, float] = self.persistence.get_tallies()
        return web.json_response(tallies)


def main() -> None:
    app = App()
    app.run()

if __name__ == "__main__":
    main()
