"""Generated from Smithy shape ``com.amazonaws.quicksight#FilteredVisualsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id

FilteredVisualsList: TypeAlias = list[
    "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilteredVisualsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilteredVisualsList:
    return list(data)
