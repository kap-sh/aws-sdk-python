"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UploaderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

UploaderStatus: TypeAlias = Literal[
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


def serialize_json(value: UploaderStatus) -> str:
    return value


def deserialize_json(data: str) -> UploaderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploaderStatus value: {data!r}")
    return cast(UploaderStatus, data)
