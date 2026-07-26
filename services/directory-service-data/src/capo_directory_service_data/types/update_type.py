"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UpdateType``."""

from typing import Literal, TypeAlias, cast

UpdateType: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "REMOVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateType) -> str:
    return value


def deserialize_json(data: str) -> UpdateType:
    return cast(UpdateType, data)
