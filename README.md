# Document API

Azure Functions based document API.

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy the sample local settings:

```powershell
Copy-Item local.settings.sample.json local.settings.json
```

For local Firebase access, place the service account file at:

```txt
serviceAccountKey.json
```

or update `FIREBASE_KEY_PATH` in `local.settings.json`.

## Run Locally

```powershell
func start
```

Health check:

```powershell
curl http://localhost:7071/api/health
```

NID document route:

```powershell
curl "http://localhost:7071/api/documents/nid_document?nid=123"
```

## Project Structure

```txt
function_app.py              Azure Functions entrypoint
config.py                    Environment settings
documents/                   Document handlers, models, and route registry
database/firebase.py          Firebase initialization and Firestore access
host.json                    Azure Functions host config
requirements.txt             Python dependencies
```

## Add A Document Route

Create a handler in `documents/`, then register it in `documents/document_routes.py`.

Example:

```python
from documents.nid_document import handle as handle_nid_document

DOCUMENT_ROUTES = {
    "nid_document": handle_nid_document,
}
```

The route key becomes the URL path:

```txt
/api/documents/{document_type}
```
