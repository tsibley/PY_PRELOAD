# `LD_PRELOAD` for Python

## `PY_PRELOAD`

Use the `PY_PRELOAD` environment variable to execute a snippet of Python code
early in interpreter startup, e.g.:

    $ PY_PRELOAD='print("👀")' python -c 'print("hello world")'
    👀
    hello world

Before you can use `PY_PRELOAD`, you must first copy `usercustomize.py` into
your user site directory, e.g.:

    cp -v usercustomize.py "$(python -c 'import site; print(site.USER_SITE)')"

Alternatively, you can install it as `sitecustomize.py` in [a user or system
site directory](https://docs.python.org/3/library/site.html).


## `pypreload`

Use the `pypreload` program to exec-chain into another program (presumably
written in Python) after arranging for a snippet of Python code to be executed
early in interpreter startup, e.g.:

    pypreload 'print("👀")' python -c 'print("hello world")'

`pypreload` accomplishes this by creating a new temporary directory, writing a
`sitecustomize.py` file to it with the given code snippet (plus some
bookkeeping), and prepending the directory to `PYTHONPATH`.  After these
arrangements are made, `pypreload` exec-chains into the other program (given as
the remaining arguments).
