"""Generated from Smithy shape ``com.amazonaws.apigateway#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER_ACCOUNTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    return cast(ResourceOwner, data)
