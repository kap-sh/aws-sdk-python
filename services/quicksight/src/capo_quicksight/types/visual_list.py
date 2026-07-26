"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.visual

VisualList: TypeAlias = list["capo_quicksight.types.visual.Visual"]


# --- restJson1 ser/de ---
def serialize_json(value: VisualList) -> list:
    import capo_quicksight.types.visual

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualList:
    import capo_quicksight.types.visual

    out: VisualList = []
    for item in data:
        out.append(capo_quicksight.types.visual.deserialize_json(item))
    return out
