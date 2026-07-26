"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsInitializationVectorInManifest``."""

from typing import Literal, TypeAlias, cast

"""The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest."""
HlsInitializationVectorInManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsInitializationVectorInManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsInitializationVectorInManifest:
    return cast(HlsInitializationVectorInManifest, data)
