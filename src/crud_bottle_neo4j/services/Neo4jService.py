from neo4j import GraphDatabase
from typing import Any
from crud_bottle_neo4j.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class Neo4jService:
    def __init__(self) -> None:
        self.driver = GraphDatabase.driver(
            NEO4J_URI, auth = (NEO4J_USER, NEO4J_PASSWORD)
        )

    def run(self, query: str, parameters: dict) -> list[dict[str, Any]]:
        with self.driver.session() as session:
            return session.run(query, parameters or {}).data()
        
    def close(self) -> None:
        self.driver.close()