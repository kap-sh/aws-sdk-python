"""Generated from Smithy shape ``com.amazonaws.xray#RetrievalStatus``."""

from typing import Literal, TypeAlias, cast

RetrievalStatus: TypeAlias = Literal[
    "SCHEDULED",
    "RUNNING",
    "COMPLETE",
    "FAILED",
    "CANCELLED",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrievalStatus:
    return cast(RetrievalStatus, data)
