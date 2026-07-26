"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlSeverity``."""

from typing import Literal, TypeAlias, cast

ControlSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSeverity) -> str:
    return value


def deserialize_json(data: str) -> ControlSeverity:
    return cast(ControlSeverity, data)
