"""Generated from Smithy shape ``com.amazonaws.connect#ContactRecordingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactRecordingType: TypeAlias = Literal[
    "AGENT",
    "IVR",
    "SCREEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "IVR",
        "SCREEN",
    )
)


def serialize_json(value: ContactRecordingType) -> str:
    return value


def deserialize_json(data: str) -> ContactRecordingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactRecordingType value: {data!r}")
    return cast(ContactRecordingType, data)
