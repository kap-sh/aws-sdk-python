"""Generated from Smithy shape ``com.amazonaws.location#PlaceSupplementalCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.place_supplemental_category

PlaceSupplementalCategoryList: TypeAlias = list[
    "capo_location.types.place_supplemental_category.PlaceSupplementalCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceSupplementalCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> PlaceSupplementalCategoryList:
    return list(data)
