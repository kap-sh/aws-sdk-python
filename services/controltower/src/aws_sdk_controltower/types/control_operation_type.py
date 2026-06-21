"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationType``."""

from typing import Literal, TypeAlias, cast

ControlOperationType: TypeAlias = Literal[
    "ENABLE_CONTROL",
    "DISABLE_CONTROL",
    "UPDATE_ENABLED_CONTROL",
    "RESET_ENABLED_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationType) -> str:
    return value


def deserialize_json(data: str) -> ControlOperationType:
    return cast(ControlOperationType, data)
