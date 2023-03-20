from os import environ

PY_PRELOAD = environ.get("PY_PRELOAD")

if PY_PRELOAD is not None:
    exec(PY_PRELOAD)
