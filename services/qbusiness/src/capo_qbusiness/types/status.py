"""Generated from Smithy shape ``com.amazonaws.qbusiness#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
