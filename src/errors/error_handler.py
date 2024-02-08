from src.views.http_types.http_response import HttpResponse

def handle_erros(error: Exception):
    return HttpResponse(
        status_code=500,
        body= {
            "erros": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
