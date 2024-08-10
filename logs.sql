CREATE TABLE logs (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMPTZ,
  service_name VARCHAR(255),
  log_level VARCHAR(50),
  message TEXT
);