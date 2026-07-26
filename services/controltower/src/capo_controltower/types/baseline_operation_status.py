"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperationStatus``."""

from typing import Literal, TypeAlias, cast

BaselineOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: BaselineOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> BaselineOperationStatus:
    return cast(BaselineOperationStatus, data)
