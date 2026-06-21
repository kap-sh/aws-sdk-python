"""Generated from Smithy shape ``com.amazonaws.detective#Severity``."""

from typing import Literal, TypeAlias, cast

Severity: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    return cast(Severity, data)
