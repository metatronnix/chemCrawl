import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


INSTALLED_APPS = [
    'rest_framework',
    'pubchem_crawler'
]

# Optional: allow localhost frontend dev
CORS_ALLOW_ALL_ORIGINS = True

# Just keep an in-memory database for now.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}