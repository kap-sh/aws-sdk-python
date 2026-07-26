"""Generated from Smithy shape ``com.amazonaws.medialive#HlsManifestDurationFormat``."""

from typing import Literal, TypeAlias, cast

"""Hls Manifest Duration Format"""
HlsManifestDurationFormat: TypeAlias = Literal[
    "FLOATING_POINT",
    "INTEGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifestDurationFormat) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestDurationFormat:
    return cast(HlsManifestDurationFormat, data)
