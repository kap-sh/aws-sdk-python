"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SearchListingsSortBy: TypeAlias = Literal[
    "RELEVANCE",
    "AVERAGE_CUSTOMER_RATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RELEVANCE",
        "AVERAGE_CUSTOMER_RATING",
    )
)


def serialize_json(value: SearchListingsSortBy) -> str:
    return value


def deserialize_json(data: str) -> SearchListingsSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchListingsSortBy value: {data!r}")
    return cast(SearchListingsSortBy, data)
