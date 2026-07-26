"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "PREPARING",
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
