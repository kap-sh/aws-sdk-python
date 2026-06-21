"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafInitializationVectorInManifest``."""

from typing import Literal, TypeAlias, cast

"""When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests."""
CmafInitializationVectorInManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafInitializationVectorInManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafInitializationVectorInManifest:
    return cast(CmafInitializationVectorInManifest, data)
