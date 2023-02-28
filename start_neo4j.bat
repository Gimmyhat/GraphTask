docker run ^
--name my-neo4j-container ^
-p 7474:7474 -p 7687:7687 ^
-v C:\Users\Sasha\neo4j\data:/data ^
-v C:\Users\Sasha\neo4j\logs:/logs ^
-e NEO4J_AUTH=neo4j/0123456789 ^
-d neo4j