"""Generated from Smithy shape ``com.amazonaws.imagebuilder#MarketplaceResourceType``."""

from typing import Literal, TypeAlias, cast

MarketplaceResourceType: TypeAlias = Literal[
    "COMPONENT_DATA",
    "COMPONENT_ARTIFACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceResourceType) -> str:
    return value


def deserialize_json(data: str) -> MarketplaceResourceType:
    return cast(MarketplaceResourceType, data)
