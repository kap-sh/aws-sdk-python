"""Generated from Smithy shape ``com.amazonaws.quicksight#IngestionStatus``."""

from typing import Literal, TypeAlias, cast

IngestionStatus: TypeAlias = Literal[
    "INITIALIZED",
    "QUEUED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionStatus:
    return cast(IngestionStatus, data)
