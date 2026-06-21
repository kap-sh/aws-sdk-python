"""Generated from Smithy shape ``com.amazonaws.controltower#EnablementStatus``."""

from typing import Literal, TypeAlias, cast

EnablementStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "UNDER_CHANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EnablementStatus:
    return cast(EnablementStatus, data)
