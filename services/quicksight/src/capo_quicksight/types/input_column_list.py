"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.input_column

InputColumnList: TypeAlias = list["capo_quicksight.types.input_column.InputColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: InputColumnList) -> list:
    import capo_quicksight.types.input_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.input_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputColumnList:
    import capo_quicksight.types.input_column

    out: InputColumnList = []
    for item in data:
        out.append(capo_quicksight.types.input_column.deserialize_json(item))
    return out
