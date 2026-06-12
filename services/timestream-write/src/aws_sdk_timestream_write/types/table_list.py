"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.table

TableList: TypeAlias = list["aws_sdk_timestream_write.types.table.Table"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableList) -> list:
    import aws_sdk_timestream_write.types.table

    out: list = []
    for item in value:
        out.append(aws_sdk_timestream_write.types.table.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TableList:
    import aws_sdk_timestream_write.types.table

    out: TableList = []
    for item in data:
        out.append(aws_sdk_timestream_write.types.table.deserialize_aws_json_1_0(item))
    return out
