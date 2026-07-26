"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingBadgeType``."""

from typing import Literal, TypeAlias, cast

ListingBadgeType: TypeAlias = Literal[
    "AWS_FREE_TIER",
    "FREE_TRIAL",
    "DEPLOYED_ON_AWS",
    "QUICK_LAUNCH",
    "MULTI_PRODUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingBadgeType) -> str:
    return value


def deserialize_json(data: str) -> ListingBadgeType:
    return cast(ListingBadgeType, data)
