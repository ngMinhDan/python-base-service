"""
usage 
all endpoints will have init_config method to initialize the config
init_config : maybe have no auto-complete code :v 
"""

from .mongo_client import MongoClient
from config import app_config
from app.models.user_models import User

class EndpointManager:
    def __init__(self) -> None:
        self.mongo = MongoClient()

    def init_config(self, config):
        self.mongo.init_config(config["MONGODB"])

    async def connect(self):
        await self.mongo.connect([User])
    
    async def disconnect(self):
        await self.mongo.disconnect()


endpoint_manager = EndpointManager()
endpoint_manager.init_config(app_config)