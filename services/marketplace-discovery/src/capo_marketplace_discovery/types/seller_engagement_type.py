"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagementType``."""

from typing import Literal, TypeAlias, cast

SellerEngagementType: TypeAlias = Literal[
    "REQUEST_FOR_PRIVATE_OFFER",
    "REQUEST_FOR_DEMO",
]


# --- restJson1 ser/de ---
def serialize_json(value: SellerEngagementType) -> str:
    return value


def deserialize_json(data: str) -> SellerEngagementType:
    return cast(SellerEngagementType, data)
