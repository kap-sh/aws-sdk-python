"""Generated from Smithy shape ``com.amazonaws.glacier#Permission``."""

from typing import Literal, TypeAlias, cast

Permission: TypeAlias = Literal[
    "FULL_CONTROL",
    "WRITE",
    "WRITE_ACP",
    "READ",
    "READ_ACP",
]


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    return cast(Permission, data)
