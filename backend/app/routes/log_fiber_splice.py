from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SpliceEntry(BaseModel):
    crew_name: str
    segment_id: str
    splice_type: str
    timestamp: str
    notes: str | None = None

@router.post("/api/splice")
def log_splice(entry: SpliceEntry):
    return {"status": "ok", "data": entry}
