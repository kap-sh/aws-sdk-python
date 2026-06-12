"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_value

DataTableValueList: TypeAlias = list[
    "aws_sdk_connect.types.data_table_value.DataTableValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueList) -> list:
    import aws_sdk_connect.types.data_table_value

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.data_table_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableValueList:
    import aws_sdk_connect.types.data_table_value

    out: DataTableValueList = []
    for item in data:
        out.append(aws_sdk_connect.types.data_table_value.deserialize_json(item))
    return out
