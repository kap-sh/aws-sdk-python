"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.output_column

OutputColumnList: TypeAlias = list["capo_quicksight.types.output_column.OutputColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnList) -> list:
    import capo_quicksight.types.output_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.output_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputColumnList:
    import capo_quicksight.types.output_column

    out: OutputColumnList = []
    for item in data:
        out.append(capo_quicksight.types.output_column.deserialize_json(item))
    return out
