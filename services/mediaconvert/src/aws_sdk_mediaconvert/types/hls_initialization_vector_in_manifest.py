"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsInitializationVectorInManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest."""
HlsInitializationVectorInManifest: TypeAlias = Literal[
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


def serialize_json(value: HlsInitializationVectorInManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsInitializationVectorInManifest:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HlsInitializationVectorInManifest value: {data!r}"
        )
    return cast(HlsInitializationVectorInManifest, data)
