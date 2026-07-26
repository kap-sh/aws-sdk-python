"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "LATEST",
    "STALE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
