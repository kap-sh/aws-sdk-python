"""Generated from Smithy shape ``com.amazonaws.artifact#AcceptanceType``."""

from typing import Literal, TypeAlias, cast

AcceptanceType: TypeAlias = Literal[
    "PASSTHROUGH",
    "EXPLICIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptanceType) -> str:
    return value


def deserialize_json(data: str) -> AcceptanceType:
    return cast(AcceptanceType, data)
