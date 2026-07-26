"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkType``."""

from typing import Literal, TypeAlias, cast

FrameworkType: TypeAlias = Literal[
    "Standard",
    "Custom",
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkType) -> str:
    return value


def deserialize_json(data: str) -> FrameworkType:
    return cast(FrameworkType, data)
