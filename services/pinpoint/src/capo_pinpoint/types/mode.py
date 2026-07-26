"""Generated from Smithy shape ``com.amazonaws.pinpoint#Mode``."""

from typing import Literal, TypeAlias, cast

Mode: TypeAlias = Literal[
    "DELIVERY",
    "FILTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    return cast(Mode, data)
