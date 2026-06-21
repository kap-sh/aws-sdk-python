"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationStatus``."""

from typing import Literal, TypeAlias, cast

OperationStatus: TypeAlias = Literal[
    "INPROGRESS",
    "SUCCESS",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
