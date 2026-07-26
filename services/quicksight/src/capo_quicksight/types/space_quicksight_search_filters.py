"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuicksightSearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.space_quicksight_search_filter

SpaceQuicksightSearchFilters: TypeAlias = list[
    "capo_quicksight.types.space_quicksight_search_filter.SpaceQuicksightSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuicksightSearchFilters) -> list:
    import capo_quicksight.types.space_quicksight_search_filter

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.space_quicksight_search_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SpaceQuicksightSearchFilters:
    import capo_quicksight.types.space_quicksight_search_filter

    out: SpaceQuicksightSearchFilters = []
    for item in data:
        out.append(
            capo_quicksight.types.space_quicksight_search_filter.deserialize_json(item)
        )
    return out
