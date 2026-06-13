"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

SellerEngagementType: TypeAlias = Literal[
    "REQUEST_FOR_PRIVATE_OFFER",
    "REQUEST_FOR_DEMO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST_FOR_PRIVATE_OFFER",
        "REQUEST_FOR_DEMO",
    )
)


def serialize_json(value: SellerEngagementType) -> str:
    return value


def deserialize_json(data: str) -> SellerEngagementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SellerEngagementType value: {data!r}")
    return cast(SellerEngagementType, data)
