from fastapi import FastAPI
from app.routes import public_router, internal_router
from app.endpoint import endpoint_manager as endpoint


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to the endpoint : DB, redis, etc...
    await endpoint.connect()
    try:
        yield
    finally:
        # graceful stop: disconnect from the endpoint
        await endpoint.disconnect()


def create_app():
    app = FastAPI(lifespan=lifespan, debug=True)
    app.include_router(public_router)
    app.include_router(internal_router)
    return app