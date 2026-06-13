"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AudioExtractionType: TypeAlias = Literal[
    "TRANSCRIPT",
    "SUMMARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRANSCRIPT",
        "SUMMARY",
    )
)


def serialize_json(value: AudioExtractionType) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioExtractionType value: {data!r}")
    return cast(AudioExtractionType, data)
