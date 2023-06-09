# cofigration file equal to setting.py in django

class Config:
    @staticmethod
    def init_app():
     pass
 
class DevelopConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class ProductionConfig(Config):
    DEBUG=False
    # postgresql://username:password@localhost:portnumber/databasename
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/posts"
    
project_config = {
    "production": ProductionConfig,
    "development": DevelopConfig
}

