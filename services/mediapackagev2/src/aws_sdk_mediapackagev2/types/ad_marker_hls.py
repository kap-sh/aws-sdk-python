"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerHls``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

AdMarkerHls: TypeAlias = Literal[
    "DATERANGE",
    "SCTE35_ENHANCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATERANGE",
        "SCTE35_ENHANCED",
    )
)


def serialize_json(value: AdMarkerHls) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerHls:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkerHls value: {data!r}")
    return cast(AdMarkerHls, data)
