"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsManifestCompression``."""

from typing import Literal, TypeAlias, cast

"""When set to GZIP, compresses HLS playlist."""
HlsManifestCompression: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsManifestCompression) -> str:
    return value


def deserialize_json(data: str) -> HlsManifestCompression:
    return cast(HlsManifestCompression, data)
