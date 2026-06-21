"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlState``."""

from typing import Literal, TypeAlias, cast

ControlState: TypeAlias = Literal[
    "ACTIVE",
    "END_OF_SUPPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlState) -> str:
    return value


def deserialize_json(data: str) -> ControlState:
    return cast(ControlState, data)
