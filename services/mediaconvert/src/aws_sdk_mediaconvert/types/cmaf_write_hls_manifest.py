"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafWriteHLSManifest``."""

from typing import Literal, TypeAlias, cast

"""When set to ENABLED, an Apple HLS manifest will be generated for this output."""
CmafWriteHLSManifest: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafWriteHLSManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafWriteHLSManifest:
    return cast(CmafWriteHLSManifest, data)
