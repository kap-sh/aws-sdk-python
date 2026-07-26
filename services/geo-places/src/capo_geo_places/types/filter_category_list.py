"""Generated from Smithy shape ``com.amazonaws.geoplaces#FilterCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string

FilterCategoryList: TypeAlias = list[
    "capo_geo_places.types.sensitive_string.SensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterCategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterCategoryList:
    return list(data)
