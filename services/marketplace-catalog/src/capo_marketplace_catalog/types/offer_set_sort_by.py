"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetSortBy``."""

from typing import Literal, TypeAlias, cast

OfferSetSortBy: TypeAlias = Literal[
    "Name",
    "State",
    "ReleaseDate",
    "SolutionId",
    "EntityId",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetSortBy) -> str:
    return value


def deserialize_json(data: str) -> OfferSetSortBy:
    return cast(OfferSetSortBy, data)
