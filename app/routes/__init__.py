from fastapi import APIRouter

from .health_routes import router as health_router
from .admin_routes import router as admin_router

# public router
public_router = APIRouter(prefix="/api/v1")
public_router.include_router(health_router)

# internal router - only for admin, you can setup more security here
# in VPN, or in the network level
internal_router = APIRouter(prefix="/internal/api/v1")
internal_router.include_router(admin_router)


