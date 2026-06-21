"""Generated from Smithy shape ``com.amazonaws.connect#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal[
    "SECONDS",
    "COUNT",
    "PERCENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    return cast(Unit, data)
