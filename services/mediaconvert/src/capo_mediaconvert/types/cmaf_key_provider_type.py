"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafKeyProviderType``."""

from typing import Literal, TypeAlias, cast

"""Specify whether your DRM encryption key is static or from a key provider that follows the SPEKE standard. For more information about SPEKE, see https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html."""
CmafKeyProviderType: TypeAlias = Literal[
    "SPEKE",
    "STATIC_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafKeyProviderType) -> str:
    return value


def deserialize_json(data: str) -> CmafKeyProviderType:
    return cast(CmafKeyProviderType, data)
