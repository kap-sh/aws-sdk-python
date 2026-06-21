"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Scope``."""

from typing import Literal, TypeAlias, cast

Scope: TypeAlias = Literal[
    "PROFILE",
    "DOMAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scope) -> str:
    return value


def deserialize_json(data: str) -> Scope:
    return cast(Scope, data)
