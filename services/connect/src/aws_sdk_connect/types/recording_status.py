"""Generated from Smithy shape ``com.amazonaws.connect#RecordingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RecordingStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETED",
    )
)


def serialize_json(value: RecordingStatus) -> str:
    return value


def deserialize_json(data: str) -> RecordingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordingStatus value: {data!r}")
    return cast(RecordingStatus, data)
