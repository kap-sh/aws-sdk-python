"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsAdMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ad marker for Apple HLS manifest."""
HlsAdMarkers: TypeAlias = Literal[
    "ELEMENTAL",
    "ELEMENTAL_SCTE35",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ELEMENTAL",
        "ELEMENTAL_SCTE35",
    )
)


def serialize_json(value: HlsAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> HlsAdMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAdMarkers value: {data!r}")
    return cast(HlsAdMarkers, data)
