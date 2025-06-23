from fastapi import FastAPI
from app.routes import log_fiber_splice

app = FastAPI(title="PML MCP Fiber Tracker")

app.include_router(log_fiber_splice.router)
