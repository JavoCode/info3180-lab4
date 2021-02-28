import os


class config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123'
    UPLOAD_FOLDER = './uploads'


class DevelopmentConfig(config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
