"""Generated from Smithy shape ``com.amazonaws.qbusiness#VideoExtractionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

VideoExtractionType: TypeAlias = Literal[
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


def serialize_json(value: VideoExtractionType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoExtractionType value: {data!r}")
    return cast(VideoExtractionType, data)
