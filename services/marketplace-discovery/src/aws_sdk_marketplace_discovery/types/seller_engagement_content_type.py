"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagementContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SellerEngagementContentType: TypeAlias = Literal["LINK",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINK",))


def serialize_json(value: SellerEngagementContentType) -> str:
    return value


def deserialize_json(data: str) -> SellerEngagementContentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SellerEngagementContentType value: {data!r}"
        )
    return cast(SellerEngagementContentType, data)
