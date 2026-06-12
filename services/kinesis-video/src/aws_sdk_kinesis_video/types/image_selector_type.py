"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ImageSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ImageSelectorType: TypeAlias = Literal[
    "SERVER_TIMESTAMP",
    "PRODUCER_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER_TIMESTAMP",
        "PRODUCER_TIMESTAMP",
    )
)


def serialize_json(value: ImageSelectorType) -> str:
    return value


def deserialize_json(data: str) -> ImageSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSelectorType value: {data!r}")
    return cast(ImageSelectorType, data)
