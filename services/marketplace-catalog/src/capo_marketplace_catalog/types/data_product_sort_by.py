"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductSortBy``."""

from typing import Literal, TypeAlias, cast

DataProductSortBy: TypeAlias = Literal[
    "EntityId",
    "ProductTitle",
    "Visibility",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> DataProductSortBy:
    return cast(DataProductSortBy, data)
