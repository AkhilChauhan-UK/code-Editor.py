services:
  - type: web
    name: django-python-editor
    env: python
    buildCommand: ""
    startCommand: gunicorn yourproject.wsgi
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: yourproject.settings
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        fromDatabase:
          name: django-db
          property: connectionString

databases:
  - name: django-db
    plan: free
