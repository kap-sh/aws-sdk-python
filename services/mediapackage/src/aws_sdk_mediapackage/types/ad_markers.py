"""Generated from Smithy shape ``com.amazonaws.mediapackage#AdMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

AdMarkers: TypeAlias = Literal[
    "NONE",
    "SCTE35_ENHANCED",
    "PASSTHROUGH",
    "DATERANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SCTE35_ENHANCED",
        "PASSTHROUGH",
        "DATERANGE",
    )
)


def serialize_json(value: AdMarkers) -> str:
    return value


def deserialize_json(data: str) -> AdMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkers value: {data!r}")
    return cast(AdMarkers, data)
