from src.views.http_types.http_response import HttpResponse
from src.errors.erro_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_erros(error: Exception):
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code = error.status_code,
            body= {
                "erros": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body= {
            "erros": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
