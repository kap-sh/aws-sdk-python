"""Generated from Smithy shape ``com.amazonaws.athena#ColumnInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.column_info

ColumnInfoList: TypeAlias = list["aws_sdk_athena.types.column_info.ColumnInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnInfoList) -> list:
    import aws_sdk_athena.types.column_info

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.column_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnInfoList:
    import aws_sdk_athena.types.column_info

    out: ColumnInfoList = []
    for item in data:
        out.append(aws_sdk_athena.types.column_info.deserialize_aws_json_1_1(item))
    return out
