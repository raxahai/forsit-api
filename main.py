from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
import routes.product as product_router
import routes.home as home_router
from config.properties import config
from exceptions.base import CustomException


def init_routers(app: FastAPI) -> None:
    app.include_router(product_router.router)
    app.include_router(home_router.router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exception: CustomException):
        return JSONResponse(
            status_code=exception.code,
            content={"error_code": exception.error_code,
                     "error_message": exception.message},
        )


def create_app() -> FastAPI:
    app = FastAPI(title="Forsit backend",
                  description="This is a test by Forsit", version="0.0.1", debug=config.DEBUG)
    init_listeners(app=app)
    init_routers(app=app)
    return app


app: FastAPI = create_app()
