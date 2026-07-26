"""Generated from Smithy shape ``com.amazonaws.ivs#RenditionConfigurationRendition``."""

from typing import Literal, TypeAlias, cast

RenditionConfigurationRendition: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
    "LOWEST_RESOLUTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RenditionConfigurationRendition) -> str:
    return value


def deserialize_json(data: str) -> RenditionConfigurationRendition:
    return cast(RenditionConfigurationRendition, data)
