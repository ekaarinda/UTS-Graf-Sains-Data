
from getpass import getpass
from neo4j import GraphDatabase

URI = "bolt://127.0.0.1:7687"
DATABASE = "neo4j"
USERNAME = "neo4j"


def add_friend(driver, name, friend_name):
    with driver.session(database=DATABASE) as session:
        session.run(
            "MERGE (a:Person {name: $name}) "
            "MERGE (friend:Person {name: $friend_name}) "
            "MERGE (a)-[:KNOWS]->(friend)",
            name=name,
            friend_name=friend_name
        ).consume()


def print_friends(driver, name):
    with driver.session(database=DATABASE) as session:
        records = session.run(
            "MATCH (a:Person)-[:KNOWS]->(friend) "
            "WHERE a.name = $name "
            "RETURN friend.name AS teman "
            "ORDER BY teman",
            name=name
        )

        for record in records:
            print(record["teman"])


password = getpass("Password Neo4j: ")

driver = GraphDatabase.driver(
    URI, auth=(USERNAME, password)
)

try:
    add_friend(driver, "Arthur", "Guinevere")
    add_friend(driver, "Arthur", "Lancelot")
    add_friend(driver, "Arthur", "Merlin")

    print("Daftar teman Arthur:")
    print_friends(driver, "Arthur")

finally:
    driver.close()
