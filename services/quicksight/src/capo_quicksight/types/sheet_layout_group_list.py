"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_layout_group

SheetLayoutGroupList: TypeAlias = list[
    "capo_quicksight.types.sheet_layout_group.SheetLayoutGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroupList) -> list:
    import capo_quicksight.types.sheet_layout_group

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet_layout_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetLayoutGroupList:
    import capo_quicksight.types.sheet_layout_group

    out: SheetLayoutGroupList = []
    for item in data:
        out.append(capo_quicksight.types.sheet_layout_group.deserialize_json(item))
    return out
