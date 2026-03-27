# for this, i am using uv instead of pip. I did uv init . and it created a req file in .toml file which gets updated when i install any package using uv. It is a great tool for managing dependencies and virtual environments in Python projects.

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host = "0.0.0.0", port = 8000, reload = True)
