"""Generated from Smithy shape ``com.amazonaws.timestreamquery#SelectColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.select_column

SelectColumnList: TypeAlias = list[
    "capo_timestream_query.types.select_column.SelectColumn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SelectColumnList) -> list:
    import capo_timestream_query.types.select_column

    out: list = []
    for item in value:
        out.append(
            capo_timestream_query.types.select_column.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SelectColumnList:
    import capo_timestream_query.types.select_column

    out: SelectColumnList = []
    for item in data:
        out.append(
            capo_timestream_query.types.select_column.deserialize_aws_json_1_0(item)
        )
    return out
