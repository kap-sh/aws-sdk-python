"""Generated from Smithy shape ``com.amazonaws.glacier#StatusCode``."""

from typing import Literal, TypeAlias, cast

StatusCode: TypeAlias = Literal[
    "InProgress",
    "Succeeded",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusCode) -> str:
    return value


def deserialize_json(data: str) -> StatusCode:
    return cast(StatusCode, data)
