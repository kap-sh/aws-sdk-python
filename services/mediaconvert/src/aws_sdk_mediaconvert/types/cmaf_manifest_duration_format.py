"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafManifestDurationFormat``."""

from typing import Literal, TypeAlias, cast

"""Indicates whether the output manifest should use floating point values for segment duration."""
CmafManifestDurationFormat: TypeAlias = Literal[
    "FLOATING_POINT",
    "INTEGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafManifestDurationFormat) -> str:
    return value


def deserialize_json(data: str) -> CmafManifestDurationFormat:
    return cast(CmafManifestDurationFormat, data)
