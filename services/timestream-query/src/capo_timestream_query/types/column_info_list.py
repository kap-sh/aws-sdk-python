"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ColumnInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.column_info

ColumnInfoList: TypeAlias = list["capo_timestream_query.types.column_info.ColumnInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ColumnInfoList) -> list:
    import capo_timestream_query.types.column_info

    out: list = []
    for item in value:
        out.append(capo_timestream_query.types.column_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ColumnInfoList:
    import capo_timestream_query.types.column_info

    out: ColumnInfoList = []
    for item in data:
        out.append(
            capo_timestream_query.types.column_info.deserialize_aws_json_1_0(item)
        )
    return out
