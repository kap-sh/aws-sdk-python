"""Generated from Smithy shape ``com.amazonaws.connect#OverrideType``."""

from typing import Literal, TypeAlias, cast

OverrideType: TypeAlias = Literal[
    "STANDARD",
    "OPEN",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideType) -> str:
    return value


def deserialize_json(data: str) -> OverrideType:
    return cast(OverrideType, data)
