"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_filter_place_type

AutocompleteFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.autocomplete_filter_place_type.AutocompleteFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteFilterPlaceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutocompleteFilterPlaceTypeList:
    return list(data)
