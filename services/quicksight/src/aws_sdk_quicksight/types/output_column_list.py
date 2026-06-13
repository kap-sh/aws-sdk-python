"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.output_column

OutputColumnList: TypeAlias = list[
    "aws_sdk_quicksight.types.output_column.OutputColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnList) -> list:
    import aws_sdk_quicksight.types.output_column

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.output_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputColumnList:
    import aws_sdk_quicksight.types.output_column

    out: OutputColumnList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.output_column.deserialize_json(item))
    return out
