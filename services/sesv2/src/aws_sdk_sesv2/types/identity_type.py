"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityType``."""

from typing import Literal, TypeAlias, cast

IdentityType: TypeAlias = Literal[
    "EMAIL_ADDRESS",
    "DOMAIN",
    "MANAGED_DOMAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    return cast(IdentityType, data)
