"""Generated from Smithy shape ``com.amazonaws.greengrass#Permission``."""

from typing import Literal, TypeAlias, cast

"""The type of permission a function has to access a resource."""
Permission: TypeAlias = Literal[
    "ro",
    "rw",
]


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    return cast(Permission, data)
