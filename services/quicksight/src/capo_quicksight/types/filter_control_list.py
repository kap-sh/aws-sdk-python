"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterControlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.filter_control

FilterControlList: TypeAlias = list[
    "capo_quicksight.types.filter_control.FilterControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterControlList) -> list:
    import capo_quicksight.types.filter_control

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.filter_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterControlList:
    import capo_quicksight.types.filter_control

    out: FilterControlList = []
    for item in data:
        out.append(capo_quicksight.types.filter_control.deserialize_json(item))
    return out
