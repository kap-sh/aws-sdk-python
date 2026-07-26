"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "MANUFACTURER_SUPPORT",
    "MANUFACTURER_INSTRUCTIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
