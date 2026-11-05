# fastAPI basics

# FastAPI intro
# The basic concept of fastAPI, which is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

# Request and Response
# so basically when FRONTEND sends a request to the BACKEND, the BACKEND will process the request and send back a response to the FRONTEND.

# Server Client
# In this process BACKEND is the SERVER and FRONTEND is the CLIENT. The BACKEND will have a ROute which will be called by the FRONTEND to get the resposne.

# Middle
# In middle of this process is the API which is the interface between the FRONTEND and BACKEND. The API will have a route which will be called by the FRONTEND to get the response from the BACKEND.

# API
# And API is a set of rules which allows one software application to interact with another. It defines the methods and data formats that applications can use to communicate with each other.

# Database
# And API is connected with database which is the storage of data. The BACKEND will have a database which will store the data and the API will interact with the database to get the data and send it to the FRONTEND. 
# Database can be of different types like SQL, NoSQL, etc. The API will interact with the database using ORM (Object Relational Mapping) or raw SQL queries.

# Get, Post, Put, Delete
# All the get, post, put, delete requests will be handled by the API and the API will interact with the database to get the data and send it to the frotnend. The API will also handle the authentication and authorizatin of the requests. The API will also handle the validation of the requests and responses. The API will also handle the error handling and logging of the requests and responses.


# ------------
# Why FastAPI?

# FastAPI is a modern, fast (high-performance), web framework for building APIs with python 3.6+ based on standard Python type hints. The key features are:
# Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
# Fast to code: Increase the speed to develop Feature by about 200% to 300%. *
# Fewer bugs: Reduce about 40% of human (developer) induced errors. *
# Intuitive: Great editor support. Completion everywhere. Less time debugging.


# FastAPI vs Django/Flask
# FastAPI is fast, have python based structure so its easy, Automatic API documentation, and have built-in support for async programming. It is also easy to use and has a simple syntax. It is also easy to deploy and scale. It is also easy to test and debug. It is also easy to integrate with other libraries and frameworks. It is also easy to learn and use.

# Type Of Frameworks
# There are two types of frameworks in python, one is synchronous and other is asynchronous. Synchronous frameworks are like Django and Flask, which are based on WSGI (Web Server Gateway Interface) and are blocking. Asynchronous frameworks are like FastAPI, which are based on ASGI (Asynchronous Server Gateway Interface) and are non-blocking. Asynchronous frameworks are faster and more efficient than synchronous frameworks.

# Built-in Features
# Automatic API docs, async support, data validation, authentication and authorization, dependency injection, background tasks, WebSockets, GraphQL support, CORS support, etc.
