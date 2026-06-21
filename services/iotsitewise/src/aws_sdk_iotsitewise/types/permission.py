"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Permission``."""

from typing import Literal, TypeAlias, cast

Permission: TypeAlias = Literal[
    "ADMINISTRATOR",
    "VIEWER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    return cast(Permission, data)
