"""Generated from Smithy shape ``com.amazonaws.sesv2#BounceType``."""

from typing import Literal, TypeAlias, cast

BounceType: TypeAlias = Literal[
    "UNDETERMINED",
    "TRANSIENT",
    "PERMANENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BounceType) -> str:
    return value


def deserialize_json(data: str) -> BounceType:
    return cast(BounceType, data)
