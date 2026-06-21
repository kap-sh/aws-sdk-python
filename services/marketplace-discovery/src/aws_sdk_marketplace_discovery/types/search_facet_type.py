"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFacetType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SearchFacetType) -> str:
    return value


def deserialize_json(data: str) -> SearchFacetType:
    return cast(SearchFacetType, data)
