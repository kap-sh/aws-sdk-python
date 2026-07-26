"""Generated from Smithy shape ``com.amazonaws.location#FilterPlaceCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.place_category

FilterPlaceCategoryList: TypeAlias = list[
    "capo_location.types.place_category.PlaceCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterPlaceCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterPlaceCategoryList:
    return list(data)
