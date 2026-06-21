"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourcePermission``."""

from typing import Literal, TypeAlias, cast

ResourcePermission: TypeAlias = Literal[
    "FULL_PERMISSION",
    "MISSING_PERMISSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePermission) -> str:
    return value


def deserialize_json(data: str) -> ResourcePermission:
    return cast(ResourcePermission, data)
