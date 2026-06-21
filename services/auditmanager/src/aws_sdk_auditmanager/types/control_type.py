"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlType``."""

from typing import Literal, TypeAlias, cast

ControlType: TypeAlias = Literal[
    "Standard",
    "Custom",
    "Core",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlType) -> str:
    return value


def deserialize_json(data: str) -> ControlType:
    return cast(ControlType, data)
