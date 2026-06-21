"""Generated from Smithy shape ``com.amazonaws.wickr#AccessLevel``."""

from typing import Literal, TypeAlias, cast

AccessLevel: TypeAlias = Literal[
    "STANDARD",
    "PREMIUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessLevel) -> str:
    return value


def deserialize_json(data: str) -> AccessLevel:
    return cast(AccessLevel, data)
