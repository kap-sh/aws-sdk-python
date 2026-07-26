"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldSortOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options

FieldSortOptionsList: TypeAlias = list[
    "capo_quicksight.types.field_sort_options.FieldSortOptions"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldSortOptionsList) -> list:
    import capo_quicksight.types.field_sort_options

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.field_sort_options.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldSortOptionsList:
    import capo_quicksight.types.field_sort_options

    out: FieldSortOptionsList = []
    for item in data:
        out.append(capo_quicksight.types.field_sort_options.deserialize_json(item))
    return out
