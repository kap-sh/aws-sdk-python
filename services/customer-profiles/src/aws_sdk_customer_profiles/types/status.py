"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "SPLIT",
    "RETRY",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
