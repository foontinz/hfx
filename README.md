# HFX - home file exchange.

## What you can do?
Send your file from local network (or anything that can access host).

## Usage:
- `uv sync` - sync your env using uv.
- `uv run litestar run` - run app itself.

App will be ran on localhost:8000.
- `localhost:8000/` - GET to see curl hint. 
- `localhost:8000/upload` - POST/multiform to send a file. 
- `localhost:8000/schema` - to see OpenAPI spec.

