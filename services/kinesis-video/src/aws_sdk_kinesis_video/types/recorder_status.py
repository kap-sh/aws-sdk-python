"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#RecorderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

RecorderStatus: TypeAlias = Literal[
    "SUCCESS",
    "USER_ERROR",
    "SYSTEM_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "USER_ERROR",
        "SYSTEM_ERROR",
    )
)


def serialize_json(value: RecorderStatus) -> str:
    return value


def deserialize_json(data: str) -> RecorderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecorderStatus value: {data!r}")
    return cast(RecorderStatus, data)
