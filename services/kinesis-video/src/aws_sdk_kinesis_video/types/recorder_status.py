"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#RecorderStatus``."""

from typing import Literal, TypeAlias, cast

RecorderStatus: TypeAlias = Literal[
    "SUCCESS",
    "USER_ERROR",
    "SYSTEM_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecorderStatus) -> str:
    return value


def deserialize_json(data: str) -> RecorderStatus:
    return cast(RecorderStatus, data)
