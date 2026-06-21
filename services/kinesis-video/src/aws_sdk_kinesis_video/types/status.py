"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
