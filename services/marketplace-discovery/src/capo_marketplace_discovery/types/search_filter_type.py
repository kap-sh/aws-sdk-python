"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFilterType``."""

from typing import Literal, TypeAlias, cast

SearchFilterType: TypeAlias = Literal[
    "MIN_AVERAGE_CUSTOMER_RATING",
    "MAX_AVERAGE_CUSTOMER_RATING",
    "CATEGORY",
    "PUBLISHER",
    "FULFILLMENT_OPTION_TYPE",
    "PRICING_MODEL",
    "PRICING_UNIT",
    "DEPLOYED_ON_AWS",
    "NUMBER_OF_PRODUCTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterType) -> str:
    return value


def deserialize_json(data: str) -> SearchFilterType:
    return cast(SearchFilterType, data)
