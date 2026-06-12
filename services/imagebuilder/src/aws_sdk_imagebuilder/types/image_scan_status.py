"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ImageScanStatus: TypeAlias = Literal[
    "PENDING",
    "SCANNING",
    "COLLECTING",
    "COMPLETED",
    "ABANDONED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SCANNING",
        "COLLECTING",
        "COMPLETED",
        "ABANDONED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_json(value: ImageScanStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageScanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageScanStatus value: {data!r}")
    return cast(ImageScanStatus, data)
