"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

DataProductSortBy: TypeAlias = Literal[
    "EntityId",
    "ProductTitle",
    "Visibility",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EntityId",
        "ProductTitle",
        "Visibility",
        "LastModifiedDate",
    )
)


def serialize_json(value: DataProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> DataProductSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataProductSortBy value: {data!r}")
    return cast(DataProductSortBy, data)
