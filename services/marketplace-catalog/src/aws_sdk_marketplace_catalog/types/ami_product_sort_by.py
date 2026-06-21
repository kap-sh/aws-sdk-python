"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductSortBy``."""

from typing import Literal, TypeAlias, cast

AmiProductSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductTitle",
    "Visibility",
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> AmiProductSortBy:
    return cast(AmiProductSortBy, data)
