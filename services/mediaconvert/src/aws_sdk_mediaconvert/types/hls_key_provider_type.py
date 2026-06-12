"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsKeyProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html."""
HlsKeyProviderType: TypeAlias = Literal[
    "SPEKE",
    "STATIC_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPEKE",
        "STATIC_KEY",
    )
)


def serialize_json(value: HlsKeyProviderType) -> str:
    return value


def deserialize_json(data: str) -> HlsKeyProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsKeyProviderType value: {data!r}")
    return cast(HlsKeyProviderType, data)
