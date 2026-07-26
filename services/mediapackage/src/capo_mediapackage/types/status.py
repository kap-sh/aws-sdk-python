"""Generated from Smithy shape ``com.amazonaws.mediapackage#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
