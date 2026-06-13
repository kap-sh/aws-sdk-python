"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VideoExtractionStatus: TypeAlias = Literal[
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


def serialize_json(value: VideoExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoExtractionStatus value: {data!r}")
    return cast(VideoExtractionStatus, data)
