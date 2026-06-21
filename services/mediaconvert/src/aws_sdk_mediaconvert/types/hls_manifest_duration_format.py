"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsManifestDurationFormat``."""

from typing import Literal, TypeAlias, cast

"""Indicates whether the output manifest should use floating point values for segment duration."""
HlsManifestDurationFormat: TypeAlias = Literal[
    "FLOATING_POINT",
    "INTEGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifestDurationFormat) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestDurationFormat:
    return cast(HlsManifestDurationFormat, data)
