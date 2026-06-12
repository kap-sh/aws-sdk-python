"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

AmiProductSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductTitle",
    "Visibility",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EntityId",
        "LastModifiedDate",
        "ProductTitle",
        "Visibility",
    )
)


def serialize_json(value: AmiProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> AmiProductSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AmiProductSortBy value: {data!r}")
    return cast(AmiProductSortBy, data)
