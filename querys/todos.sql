CREATE TABLE IF NOT EXISTS todo (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            item VARCHAR(255) NOT NULL
        )

INSERT INTO todo (item)
VALUES ('Learn SQL'), ('Build a REST API'), ('Write Unit Tests.');

SELECT id, item
FROM todo;

UPDATE todo
SET item = 'Learn Advanced SQL'
WHERE id = '3c8b05aa-9893-4e9f-be4b-3a969e7fc726'

