"""Generated from Smithy shape ``com.amazonaws.timestreamquery#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.row

RowList: TypeAlias = list["capo_timestream_query.types.row.Row"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RowList) -> list:
    import capo_timestream_query.types.row

    out: list = []
    for item in value:
        out.append(capo_timestream_query.types.row.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RowList:
    import capo_timestream_query.types.row

    out: RowList = []
    for item in data:
        out.append(capo_timestream_query.types.row.deserialize_aws_json_1_0(item))
    return out
