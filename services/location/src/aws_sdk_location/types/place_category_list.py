"""Generated from Smithy shape ``com.amazonaws.location#PlaceCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.place_category

PlaceCategoryList: TypeAlias = list[
    "aws_sdk_location.types.place_category.PlaceCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaceCategoryList:
    return list(data)
