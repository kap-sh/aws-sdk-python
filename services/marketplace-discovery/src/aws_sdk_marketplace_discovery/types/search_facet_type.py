"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFacetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SearchFacetType: TypeAlias = Literal[
    "AVERAGE_CUSTOMER_RATING",
    "CATEGORY",
    "PUBLISHER",
    "FULFILLMENT_OPTION_TYPE",
    "PRICING_MODEL",
    "PRICING_UNIT",
    "DEPLOYED_ON_AWS",
    "NUMBER_OF_PRODUCTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVERAGE_CUSTOMER_RATING",
        "CATEGORY",
        "PUBLISHER",
        "FULFILLMENT_OPTION_TYPE",
        "PRICING_MODEL",
        "PRICING_UNIT",
        "DEPLOYED_ON_AWS",
        "NUMBER_OF_PRODUCTS",
    )
)


def serialize_json(value: SearchFacetType) -> str:
    return value


def deserialize_json(data: str) -> SearchFacetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchFacetType value: {data!r}")
    return cast(SearchFacetType, data)
