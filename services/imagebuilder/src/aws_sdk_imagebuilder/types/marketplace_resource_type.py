"""Generated from Smithy shape ``com.amazonaws.imagebuilder#MarketplaceResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

MarketplaceResourceType: TypeAlias = Literal[
    "COMPONENT_DATA",
    "COMPONENT_ARTIFACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPONENT_DATA",
        "COMPONENT_ARTIFACT",
    )
)


def serialize_json(value: MarketplaceResourceType) -> str:
    return value


def deserialize_json(data: str) -> MarketplaceResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketplaceResourceType value: {data!r}")
    return cast(MarketplaceResourceType, data)
