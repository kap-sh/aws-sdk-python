"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashUtcTimingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashUtcTimingMode: TypeAlias = Literal[
    "HTTP_HEAD",
    "HTTP_ISO",
    "HTTP_XSDATE",
    "UTC_DIRECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_HEAD",
        "HTTP_ISO",
        "HTTP_XSDATE",
        "UTC_DIRECT",
    )
)


def serialize_json(value: DashUtcTimingMode) -> str:
    return value


def deserialize_json(data: str) -> DashUtcTimingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashUtcTimingMode value: {data!r}")
    return cast(DashUtcTimingMode, data)
