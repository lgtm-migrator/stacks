# stacks.settings.base
# Default Django settings for entire Stacks project
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Apr 22 14:10:32 2015 -0400
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: base.py [] benjamin@bengfort.com $

"""
Django settings for stacks project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os

##########################################################################
## Helper function for environmental settings
##########################################################################


def environ_setting(name, default=None):
    """
    Fetch setting from the environment- if not found, then this setting is
    ImproperlyConfigured.
    """
    if name not in os.environ and default is None:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(
            "The {0} ENVVAR is not set.".format(name)
        )

    return os.environ.get(name, default)


##########################################################################
## Build Paths inside of project with os.path.join
##########################################################################

BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(BASE_DIR, os.pardir))

##########################################################################
## Secret settings - do not store!
##########################################################################

SECRET_KEY = environ_setting("SECRET_KEY")

##########################################################################
## Database Settings
##########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ_setting('DB_NAME', 'stacks'),
        'USER': environ_setting('DB_USER', 'django'),
        'PASSWORD': environ_setting('DB_PASS', ''),
        'HOST': environ_setting('DB_HOST', 'localhost'),
        'PORT': environ_setting('DB_PORT', '5432'),
    },
}

##########################################################################
## Runtime settings
##########################################################################

## Debugging Settings
DEBUG            = False

## Hosts
ALLOWED_HOSTS    = []

## WSGI Configuration
ROOT_URLCONF     = 'stacks.urls'
WSGI_APPLICATION = 'stacks.wsgi.application'


## Application definition
INSTALLED_APPS   = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps

    # Stacks apps
)

## Request Handling
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

## Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'America/New_York'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

##########################################################################
## Content (Static, Media, Templates)
##########################################################################

## Template Handling
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

## Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS    = (
    os.path.join(PROJECT_DIR, 'static'),
)

##########################################################################
## Logging and Error Reporting
##########################################################################

ADMINS          = (
    ('Benjamin Bengfort', 'benjamin@bengfort.com'),
)

SERVER_EMAIL    = environ_setting("SERVER_EMAIL", "")
EMAIL_USE_TLS   = True
EMAIL_HOST      = environ_setting("EMAIL_HOST", "")
EMAIL_HOST_USER = environ_setting("EMAIl_HOST_USER", "")
EMAIL_HOST_PASSWORD = environ_setting("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT      = 587

##########################################################################
## Grappelli Configuration
##########################################################################

GRAPPELLI_ADMIN_TITLE = "Bengfort Stacks Admin"
