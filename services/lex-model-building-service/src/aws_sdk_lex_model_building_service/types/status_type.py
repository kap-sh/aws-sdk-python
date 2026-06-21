"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StatusType``."""

from typing import Literal, TypeAlias, cast

StatusType: TypeAlias = Literal[
    "Detected",
    "Missed",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusType) -> str:
    return value


def deserialize_json(data: str) -> StatusType:
    return cast(StatusType, data)
