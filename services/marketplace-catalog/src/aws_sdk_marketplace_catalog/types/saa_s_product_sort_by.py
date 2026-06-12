"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

SaaSProductSortBy: TypeAlias = Literal[
    "EntityId",
    "ProductTitle",
    "Visibility",
    "LastModifiedDate",
    "DeliveryOptionTypes",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EntityId",
        "ProductTitle",
        "Visibility",
        "LastModifiedDate",
        "DeliveryOptionTypes",
    )
)


def serialize_json(value: SaaSProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> SaaSProductSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SaaSProductSortBy value: {data!r}")
    return cast(SaaSProductSortBy, data)
