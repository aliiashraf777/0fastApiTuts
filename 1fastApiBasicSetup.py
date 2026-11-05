# we need to install python on our device
# and then we need to install fastAPI using command "pip install fastAPI

# Pip
# pip is a package manager for python packages, or modules if you like. A package contains all the files you need for a module. Modules are Python code libraries you can include in your project.

# After that we need to install uvicorn using command "pip install uvicorn".

# Uvicorn
# Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. It is built on top of the asyncio library and is designed to be used with asynchronous web frameworks like FastAPI. Uvicorn is a production-ready server that can handle high loads and is suitable for running FastAPI applications in production environments.

# Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

# then check python --versin in your terminal
# python3 --version for macOS

# Start Project
# We need to run "python -m uvicorn main:"

# Virtual Environment
# python -m venv venv
# source venv/bin/activate for macOS
# venv\Scripts\activate for Windows

# then install your fastApi and Uvicron server in virtual environment for this specific project with command
# "pip install fastapi uvicorn"

# Swagger UI
# after staring the server on 8000 port, we can see the swagger UI on "http://localhost:8000/docs" and redoc on "http://localhost:8000/redoc"