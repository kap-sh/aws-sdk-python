"""Generated from Smithy shape ``com.amazonaws.iot#ConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

ConfidenceLevel: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceLevel:
    return cast(ConfidenceLevel, data)
