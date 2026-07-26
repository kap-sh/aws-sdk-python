"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UploaderStatus``."""

from typing import Literal, TypeAlias, cast

UploaderStatus: TypeAlias = Literal[
    "SUCCESS",
    "USER_ERROR",
    "SYSTEM_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: UploaderStatus) -> str:
    return value


def deserialize_json(data: str) -> UploaderStatus:
    return cast(UploaderStatus, data)
