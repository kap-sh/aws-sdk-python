"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationEventStatus``."""

from typing import Literal, TypeAlias, cast

OperationEventStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationEventStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationEventStatus:
    return cast(OperationEventStatus, data)
