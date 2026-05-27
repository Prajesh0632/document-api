import azure.functions as func

from config import get_settings
from documents import DOCUMENT_ROUTES
from database import init_firebase

settings = get_settings()

auth_level = (
    func.AuthLevel.FUNCTION if settings.enable_auth else func.AuthLevel.ANONYMOUS
)

app = func.FunctionApp()

init_firebase()

@app.function_name("DocumentRouter")
@app.route(route="documents/{document_type}", auth_level=auth_level)
def document_router(req: func.HttpRequest) -> func.HttpResponse:
    document_type = req.route_params.get("document_type")
    handler = DOCUMENT_ROUTES.get(document_type)

    if handler is None:
        return func.HttpResponse(
            f"Unknown document type: {document_type}",
            status_code=404,
        )

    return handler(req)


@app.function_name("Health")
@app.route(route="health")
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """Health check endpoint."""
    return func.HttpResponse(
        f"OK - Environment: {settings.environment}",
        status_code=200,
    )
