"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafManifestCompression``."""

from typing import Literal, TypeAlias, cast

"""When set to GZIP, compresses HLS playlist."""
CmafManifestCompression: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafManifestCompression) -> str:
    return value


def deserialize_json(data: str) -> CmafManifestCompression:
    return cast(CmafManifestCompression, data)
