"""Generated from Smithy shape ``com.amazonaws.quicksight#AudioExtractionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AudioExtractionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AudioExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioExtractionStatus value: {data!r}")
    return cast(AudioExtractionStatus, data)
