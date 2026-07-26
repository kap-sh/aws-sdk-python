"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationStatus``."""

from typing import Literal, TypeAlias, cast

ControlOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlOperationStatus:
    return cast(ControlOperationStatus, data)
