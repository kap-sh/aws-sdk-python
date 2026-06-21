"""Generated from Smithy shape ``com.amazonaws.ram#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER-ACCOUNTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    return cast(ResourceOwner, data)
