"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Severity``."""

from typing import Literal, TypeAlias, cast

Severity: TypeAlias = Literal[
    "Info",
    "Low",
    "Medium",
    "High",
    "Critical",
]


# --- restJson1 ser/de ---
def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    return cast(Severity, data)
