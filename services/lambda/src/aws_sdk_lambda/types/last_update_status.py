"""Generated from Smithy shape ``com.amazonaws.lambda#LastUpdateStatus``."""

from typing import Literal, TypeAlias, cast

LastUpdateStatus: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> LastUpdateStatus:
    return cast(LastUpdateStatus, data)
