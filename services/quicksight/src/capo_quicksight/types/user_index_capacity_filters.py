"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacityFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.user_index_capacity_filter

UserIndexCapacityFilters: TypeAlias = list[
    "capo_quicksight.types.user_index_capacity_filter.UserIndexCapacityFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacityFilters) -> list:
    import capo_quicksight.types.user_index_capacity_filter

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.user_index_capacity_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserIndexCapacityFilters:
    import capo_quicksight.types.user_index_capacity_filter

    out: UserIndexCapacityFilters = []
    for item in data:
        out.append(
            capo_quicksight.types.user_index_capacity_filter.deserialize_json(item)
        )
    return out
