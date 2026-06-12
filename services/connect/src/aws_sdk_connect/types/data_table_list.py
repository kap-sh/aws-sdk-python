"""Generated from Smithy shape ``com.amazonaws.connect#DataTableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table

DataTableList: TypeAlias = list["aws_sdk_connect.types.data_table.DataTable"]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableList) -> list:
    import aws_sdk_connect.types.data_table

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.data_table.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableList:
    import aws_sdk_connect.types.data_table

    out: DataTableList = []
    for item in data:
        out.append(aws_sdk_connect.types.data_table.deserialize_json(item))
    return out
