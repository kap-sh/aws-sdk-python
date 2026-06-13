"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ScanMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ScanMode: TypeAlias = Literal[
    "progressive",
    "interlace",
    "progressive-segmented-frame",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "progressive",
        "interlace",
        "progressive-segmented-frame",
    )
)


def serialize_json(value: ScanMode) -> str:
    return value


def deserialize_json(data: str) -> ScanMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanMode value: {data!r}")
    return cast(ScanMode, data)
