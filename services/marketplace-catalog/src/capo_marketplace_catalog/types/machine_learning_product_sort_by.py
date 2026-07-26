"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductSortBy``."""

from typing import Literal, TypeAlias, cast

"""<p>The fields that you can sort machine learning products by.</p>"""
MachineLearningProductSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductTitle",
    "Visibility",
]


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> MachineLearningProductSortBy:
    return cast(MachineLearningProductSortBy, data)
