"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.input_column

InputColumnList: TypeAlias = list["aws_sdk_quicksight.types.input_column.InputColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: InputColumnList) -> list:
    import aws_sdk_quicksight.types.input_column

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.input_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputColumnList:
    import aws_sdk_quicksight.types.input_column

    out: InputColumnList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.input_column.deserialize_json(item))
    return out
