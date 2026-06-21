"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Severity``."""

from typing import Literal, TypeAlias, cast

Severity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    return cast(Severity, data)
