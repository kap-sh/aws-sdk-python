"""Generated from Smithy shape ``com.amazonaws.quicksight#KbIngestionStatus``."""

from typing import Literal, TypeAlias, cast

KbIngestionStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "INCOMPLETE",
    "CANCELLED",
    "CANCELLING",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: KbIngestionStatus) -> str:
    return value


def deserialize_json(data: str) -> KbIngestionStatus:
    return cast(KbIngestionStatus, data)
