"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#AdMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage_vod.errors import DeserializationError

AdMarkers: TypeAlias = Literal[
    "NONE",
    "SCTE35_ENHANCED",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SCTE35_ENHANCED",
        "PASSTHROUGH",
    )
)


def serialize_json(value: AdMarkers) -> str:
    return value


def deserialize_json(data: str) -> AdMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkers value: {data!r}")
    return cast(AdMarkers, data)
