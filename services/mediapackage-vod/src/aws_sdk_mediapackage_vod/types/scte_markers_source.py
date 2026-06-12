"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ScteMarkersSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage_vod.errors import DeserializationError

ScteMarkersSource: TypeAlias = Literal[
    "SEGMENTS",
    "MANIFEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEGMENTS",
        "MANIFEST",
    )
)


def serialize_json(value: ScteMarkersSource) -> str:
    return value


def deserialize_json(data: str) -> ScteMarkersSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScteMarkersSource value: {data!r}")
    return cast(ScteMarkersSource, data)
