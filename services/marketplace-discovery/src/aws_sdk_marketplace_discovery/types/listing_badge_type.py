"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingBadgeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

ListingBadgeType: TypeAlias = Literal[
    "AWS_FREE_TIER",
    "FREE_TRIAL",
    "DEPLOYED_ON_AWS",
    "QUICK_LAUNCH",
    "MULTI_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_FREE_TIER",
        "FREE_TRIAL",
        "DEPLOYED_ON_AWS",
        "QUICK_LAUNCH",
        "MULTI_PRODUCT",
    )
)


def serialize_json(value: ListingBadgeType) -> str:
    return value


def deserialize_json(data: str) -> ListingBadgeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListingBadgeType value: {data!r}")
    return cast(ListingBadgeType, data)
