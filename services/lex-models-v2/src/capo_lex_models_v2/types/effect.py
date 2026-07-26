"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Effect``."""

from typing import Literal, TypeAlias, cast

Effect: TypeAlias = Literal[
    "Allow",
    "Deny",
]


# --- restJson1 ser/de ---
def serialize_json(value: Effect) -> str:
    return value


def deserialize_json(data: str) -> Effect:
    return cast(Effect, data)
