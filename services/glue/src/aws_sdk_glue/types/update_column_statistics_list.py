"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics

UpdateColumnStatisticsList: TypeAlias = list[
    "aws_sdk_glue.types.column_statistics.ColumnStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsList) -> list:
    import aws_sdk_glue.types.column_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.column_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateColumnStatisticsList:
    import aws_sdk_glue.types.column_statistics

    out: UpdateColumnStatisticsList = []
    for item in data:
        out.append(aws_sdk_glue.types.column_statistics.deserialize_aws_json_1_1(item))
    return out
