CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    description VARCHAR(100),
    temperature FLOAT,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);