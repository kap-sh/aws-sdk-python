"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsSortBy``."""

from typing import Literal, TypeAlias, cast

SearchListingsSortBy: TypeAlias = Literal[
    "RELEVANCE",
    "AVERAGE_CUSTOMER_RATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsSortBy) -> str:
    return value


def deserialize_json(data: str) -> SearchListingsSortBy:
    return cast(SearchListingsSortBy, data)
