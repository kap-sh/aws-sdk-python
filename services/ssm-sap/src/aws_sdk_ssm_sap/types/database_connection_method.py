"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseConnectionMethod``."""

from typing import Literal, TypeAlias, cast

DatabaseConnectionMethod: TypeAlias = Literal[
    "DIRECT",
    "OVERLAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseConnectionMethod) -> str:
    return value


def deserialize_json(data: str) -> DatabaseConnectionMethod:
    return cast(DatabaseConnectionMethod, data)
