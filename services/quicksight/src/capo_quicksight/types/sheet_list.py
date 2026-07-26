"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet

SheetList: TypeAlias = list["capo_quicksight.types.sheet.Sheet"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetList) -> list:
    import capo_quicksight.types.sheet

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetList:
    import capo_quicksight.types.sheet

    out: SheetList = []
    for item in data:
        out.append(capo_quicksight.types.sheet.deserialize_json(item))
    return out
