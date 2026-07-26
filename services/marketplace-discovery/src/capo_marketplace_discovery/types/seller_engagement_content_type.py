"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagementContentType``."""

from typing import Literal, TypeAlias, cast

SellerEngagementContentType: TypeAlias = Literal["LINK",]


# --- restJson1 ser/de ---
def serialize_json(value: SellerEngagementContentType) -> str:
    return value


def deserialize_json(data: str) -> SellerEngagementContentType:
    return cast(SellerEngagementContentType, data)
