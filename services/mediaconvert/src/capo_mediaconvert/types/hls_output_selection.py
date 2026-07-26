"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsOutputSelection``."""

from typing import Literal, TypeAlias, cast

"""Indicates whether the .m3u8 manifest file should be generated for this HLS output group."""
HlsOutputSelection: TypeAlias = Literal[
    "MANIFESTS_AND_SEGMENTS",
    "SEGMENTS_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsOutputSelection) -> str:
    return value


def deserialize_json(data: str) -> HlsOutputSelection:
    return cast(HlsOutputSelection, data)
