"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

"""<p>The fields that you can sort machine learning products by.</p>"""
MachineLearningProductSortBy: TypeAlias = Literal[
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


def serialize_json(value: MachineLearningProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> MachineLearningProductSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MachineLearningProductSortBy value: {data!r}"
        )
    return cast(MachineLearningProductSortBy, data)
