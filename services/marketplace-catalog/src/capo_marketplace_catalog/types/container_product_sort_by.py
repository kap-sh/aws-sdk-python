"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductSortBy``."""

from typing import Literal, TypeAlias, cast

ContainerProductSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductTitle",
    "Visibility",
    "CompatibleAWSServices",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> ContainerProductSortBy:
    return cast(ContainerProductSortBy, data)
