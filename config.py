import os

PROJECT_DIR = PROJECT_DIR = os.path.dirname(__file__)
EXPORT_DIRECTORY = os.getenv('EXPORT_DIRECTORY', 'PROJECT_DIR')
S3_BUCKET = os.getenv('S3_BUCKET', 'mlr-exports')
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
TIERNAME = os.getenv('TIERNAME', 'development')
DEBUG = False
