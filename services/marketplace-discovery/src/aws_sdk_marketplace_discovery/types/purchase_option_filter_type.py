"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

PurchaseOptionFilterType: TypeAlias = Literal[
    "PRODUCT_ID",
    "SELLER_OF_RECORD_PROFILE_ID",
    "PURCHASE_OPTION_TYPE",
    "VISIBILITY_SCOPE",
    "AVAILABILITY_STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCT_ID",
        "SELLER_OF_RECORD_PROFILE_ID",
        "PURCHASE_OPTION_TYPE",
        "VISIBILITY_SCOPE",
        "AVAILABILITY_STATUS",
    )
)


def serialize_json(value: PurchaseOptionFilterType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseOptionFilterType value: {data!r}")
    return cast(PurchaseOptionFilterType, data)
