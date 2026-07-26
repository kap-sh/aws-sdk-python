"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsSortOrder``."""

from typing import Literal, TypeAlias, cast

SearchListingsSortOrder: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsSortOrder) -> str:
    return value


def deserialize_json(data: str) -> SearchListingsSortOrder:
    return cast(SearchListingsSortOrder, data)
