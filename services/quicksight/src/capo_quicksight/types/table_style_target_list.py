"""Generated from Smithy shape ``com.amazonaws.quicksight#TableStyleTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.table_style_target

TableStyleTargetList: TypeAlias = list[
    "capo_quicksight.types.table_style_target.TableStyleTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableStyleTargetList) -> list:
    import capo_quicksight.types.table_style_target

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.table_style_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableStyleTargetList:
    import capo_quicksight.types.table_style_target

    out: TableStyleTargetList = []
    for item in data:
        out.append(capo_quicksight.types.table_style_target.deserialize_json(item))
    return out
