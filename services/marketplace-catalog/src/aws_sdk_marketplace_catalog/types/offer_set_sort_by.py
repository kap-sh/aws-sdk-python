"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

OfferSetSortBy: TypeAlias = Literal[
    "Name",
    "State",
    "ReleaseDate",
    "SolutionId",
    "EntityId",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "State",
        "ReleaseDate",
        "SolutionId",
        "EntityId",
        "LastModifiedDate",
    )
)


def serialize_json(value: OfferSetSortBy) -> str:
    return value


def deserialize_json(data: str) -> OfferSetSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferSetSortBy value: {data!r}")
    return cast(OfferSetSortBy, data)
