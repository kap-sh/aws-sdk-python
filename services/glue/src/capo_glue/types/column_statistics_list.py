"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_statistics

ColumnStatisticsList: TypeAlias = list[
    "capo_glue.types.column_statistics.ColumnStatistics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsList) -> list:
    import capo_glue.types.column_statistics

    out: list = []
    for item in value:
        out.append(capo_glue.types.column_statistics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnStatisticsList:
    import capo_glue.types.column_statistics

    out: ColumnStatisticsList = []
    for item in data:
        out.append(capo_glue.types.column_statistics.deserialize_aws_json_1_1(item))
    return out
