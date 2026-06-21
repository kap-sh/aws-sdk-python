"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseType``."""

from typing import Literal, TypeAlias, cast

DatabaseType: TypeAlias = Literal[
    "SYSTEM",
    "TENANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseType) -> str:
    return value


def deserialize_json(data: str) -> DatabaseType:
    return cast(DatabaseType, data)
