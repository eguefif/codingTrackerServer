from codingTrackerServer.session import Session
from codingTrackerServer.sqlhandler import SqlHandler
from codingTrackerServer.process import EditorProcess


class Persistence:
    def __init__( self,
            db: str = None,
            encoding: str = "utf-8",
    ) -> None:
        self.sql: SqlHandler = SqlHandler(db)
        self.encoding = encoding

    def update(self, data: list[tuple[str, float, float, bool]]):
        content: list[Session] = self._sql_format(data)
        self.sql.update(content)

    def _sql_format(self, data: list[tuple[str, float, float, bool]]) -> list[Session]:
        return [Session(language=r[0], start_time=r[1], end_time=r[2], running=r[3])
                for r in data]

    def terminate(self):
        self.sql.terminate()

    def get_tallies(self) -> dict[str, float]:
        return {"python": 23431.1, "c": 1312.1}
