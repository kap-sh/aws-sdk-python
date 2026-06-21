"""Generated from Smithy shape ``com.amazonaws.eks#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

UpdateStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Cancelled",
    "Successful",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    return cast(UpdateStatus, data)
