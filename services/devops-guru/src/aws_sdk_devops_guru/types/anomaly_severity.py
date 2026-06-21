"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalySeverity``."""

from typing import Literal, TypeAlias, cast

AnomalySeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalySeverity) -> str:
    return value


def deserialize_json(data: str) -> AnomalySeverity:
    return cast(AnomalySeverity, data)
