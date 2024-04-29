## Welcome to Python-Base-Service
A clearly fast Python's codebase for building a service to serve HTTP, SSE, WS requests. Built with love by me. In the python-base-service, I have developed the following features, with ongoing features in the pipeline with FastAPI framework. A framework give strongly features to help developer can make web/app as soon as possible in 1, 2 days.:
- [x]  Support for working with configurations (Dev, Production, Default Values) with TOML
- [x]  Support for managing logs (Format, Output, Level)
- [x]  Support tracing with OpenTelemetry
- [x]  Support for database operations (RDBMS, MongoDB)
- [x]  Support for Authentication with JWT (Sample Payload, Create, GetClaims)
- [x]  Support for working with Kafka (Schema, Broker, Consumer)
- [x]  Support for Redis operations (Connect, Get, Set, Invalidate)
- [x]  Support for AWS S3 operations (Connect, Get, Upload)
- [x]  Support for Elasticsearch (Connect, Insert, Search)
- [x]  Support for middleware (Rate Limit, Blocking)
- [x]  Easy integration with HTTP request handling (Status, 
Response, graceful shutdown)
- [X] Support common utils features with datetime, async, sync, loop
- [X] Some very helpful documentations for learn clearly PYTHON
- [ ]  Support for GRPC
- [ ]  Support for Websocket
- [ ]  Support for Ethereum

## Demo of a Basic System
I will demo a project with this structure with MVP: Chat system like Chat GPT
- [X] Support standard authentication functions (Sign In, Sign Up, Change Password, Get Profile)
- [X] Support admin functions : Get all users, Block IP, Upgrade role, Rate Limit
- [X] Support full-text search using ES's API - search message for user
- [X] Support post notifications for user - example Crypto currency like BTC, ETH, BNB with use Kafka 
- [X] API documentations 
- [X] Export Postman file


## Prerequisites
```
# must run
Python 3.11.4
python3 -m venv venv
source venv/bin/active

# For dev
make install
make run

# for deploy

```
### Thanks for visting me