"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsManifestDurationFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Indicates whether the output manifest should use floating point values for segment duration."""
HlsManifestDurationFormat: TypeAlias = Literal[
    "FLOATING_POINT",
    "INTEGER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOATING_POINT",
        "INTEGER",
    )
)


def serialize_json(value: HlsManifestDurationFormat) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestDurationFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsManifestDurationFormat value: {data!r}")
    return cast(HlsManifestDurationFormat, data)
