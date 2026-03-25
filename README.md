# payments_api_project

Bank payments REST API project.

This is a little PoC in python to test sending payments data over a REST endpoint that persists payments transactions to a postgres data store.

## Quick start after downloading

1. Unzip the file.

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the API:

```
uvicorn main:app --reload
```

4. Open the interactive API docs:

```
http://localhost:8000/docs
```

## Database setup

Before running the API you need to create the database, role, and grant the appropriate permissions in PostgreSQL.

### 1. Open the PostgreSQL command line

Connect as the postgres superuser:

```
psql -U postgres
```

### 2. Create the database

```sql
CREATE DATABASE payments_db;
```

### 3. Create the payments role with a password

```sql
CREATE ROLE payments WITH LOGIN PASSWORD 'your_password_here';
```

Replace `your_password_here` with a strong password. This should match what you set in your `.env` file.

### 4. Grant connection access to the database

```sql
GRANT CONNECT ON DATABASE payments_db TO payments;
```

### 5. Connect to the payments_db database

```
\c payments_db
```

### 6. Grant schema permissions

Allow the role to use the public schema and read/write to all tables:

```sql
GRANT USAGE ON SCHEMA public TO payments;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO payments;
```

To ensure the role also has access to any tables created in the future (e.g. after migrations):

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO payments;
```

### 7. Verify the role exists

```sql
\du
```

You should see `payments` listed in the output.

### 8. Exit the PostgreSQL prompt

```
\q
```

