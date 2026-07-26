"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.filter_group

FilterGroupList: TypeAlias = list["capo_quicksight.types.filter_group.FilterGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterGroupList) -> list:
    import capo_quicksight.types.filter_group

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.filter_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterGroupList:
    import capo_quicksight.types.filter_group

    out: FilterGroupList = []
    for item in data:
        out.append(capo_quicksight.types.filter_group.deserialize_json(item))
    return out
