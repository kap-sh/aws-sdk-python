"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

PurchaseOptionType: TypeAlias = Literal[
    "OFFER",
    "OFFERSET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFFER",
        "OFFERSET",
    )
)


def serialize_json(value: PurchaseOptionType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseOptionType value: {data!r}")
    return cast(PurchaseOptionType, data)
