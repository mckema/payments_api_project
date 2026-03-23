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

