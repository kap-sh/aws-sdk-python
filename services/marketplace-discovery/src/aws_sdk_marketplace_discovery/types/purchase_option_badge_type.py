"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadgeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

PurchaseOptionBadgeType: TypeAlias = Literal[
    "PRIVATE_PRICING",
    "FUTURE_DATED",
    "REPLACEMENT_OFFER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIVATE_PRICING",
        "FUTURE_DATED",
        "REPLACEMENT_OFFER",
    )
)


def serialize_json(value: PurchaseOptionBadgeType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionBadgeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseOptionBadgeType value: {data!r}")
    return cast(PurchaseOptionBadgeType, data)
