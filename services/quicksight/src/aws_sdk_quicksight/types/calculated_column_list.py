"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.calculated_column

CalculatedColumnList: TypeAlias = list[
    "aws_sdk_quicksight.types.calculated_column.CalculatedColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedColumnList) -> list:
    import aws_sdk_quicksight.types.calculated_column

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.calculated_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculatedColumnList:
    import aws_sdk_quicksight.types.calculated_column

    out: CalculatedColumnList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.calculated_column.deserialize_json(item))
    return out
