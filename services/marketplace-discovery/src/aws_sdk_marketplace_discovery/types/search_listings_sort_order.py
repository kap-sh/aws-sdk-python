"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SearchListingsSortOrder: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DESCENDING",
        "ASCENDING",
    )
)


def serialize_json(value: SearchListingsSortOrder) -> str:
    return value


def deserialize_json(data: str) -> SearchListingsSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchListingsSortOrder value: {data!r}")
    return cast(SearchListingsSortOrder, data)
