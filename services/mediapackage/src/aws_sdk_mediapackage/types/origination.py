"""Generated from Smithy shape ``com.amazonaws.mediapackage#Origination``."""

from typing import Literal, TypeAlias, cast

Origination: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Origination) -> str:
    return value


def deserialize_json(data: str) -> Origination:
    return cast(Origination, data)
