"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafInitializationVectorInManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you use DRM with CMAF outputs, choose whether the service writes the 128-bit encryption initialization vector in the HLS and DASH manifests."""
CmafInitializationVectorInManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: CmafInitializationVectorInManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafInitializationVectorInManifest:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CmafInitializationVectorInManifest value: {data!r}"
        )
    return cast(CmafInitializationVectorInManifest, data)
