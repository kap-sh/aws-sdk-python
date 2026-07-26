"""Generated from Smithy shape ``com.amazonaws.finspacedata#IngestionStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of the ingestion process returned from scheduler service."""
IngestionStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCESS",
    "RUNNING",
    "STOP_REQUESTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionStatus:
    return cast(IngestionStatus, data)
