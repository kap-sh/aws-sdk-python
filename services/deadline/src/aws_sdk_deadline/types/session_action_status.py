"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionStatus``."""

from typing import Literal, TypeAlias, cast

SessionActionStatus: TypeAlias = Literal[
    "ASSIGNED",
    "RUNNING",
    "CANCELING",
    "SUCCEEDED",
    "FAILED",
    "INTERRUPTED",
    "CANCELED",
    "NEVER_ATTEMPTED",
    "SCHEDULED",
    "RECLAIMING",
    "RECLAIMED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionActionStatus:
    return cast(SessionActionStatus, data)
