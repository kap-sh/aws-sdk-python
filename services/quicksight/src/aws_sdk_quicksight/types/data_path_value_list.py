"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_value

DataPathValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_path_value.DataPathValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataPathValueList) -> list:
    import aws_sdk_quicksight.types.data_path_value

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_path_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataPathValueList:
    import aws_sdk_quicksight.types.data_path_value

    out: DataPathValueList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.data_path_value.deserialize_json(item))
    return out
