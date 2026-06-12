"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

ContainerProductSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductTitle",
    "Visibility",
    "CompatibleAWSServices",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EntityId",
        "LastModifiedDate",
        "ProductTitle",
        "Visibility",
        "CompatibleAWSServices",
    )
)


def serialize_json(value: ContainerProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> ContainerProductSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerProductSortBy value: {data!r}")
    return cast(ContainerProductSortBy, data)
