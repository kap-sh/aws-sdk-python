"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics_error

ColumnStatisticsErrors: TypeAlias = list[
    "aws_sdk_glue.types.column_statistics_error.ColumnStatisticsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsErrors) -> list:
    import aws_sdk_glue.types.column_statistics_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.column_statistics_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnStatisticsErrors:
    import aws_sdk_glue.types.column_statistics_error

    out: ColumnStatisticsErrors = []
    for item in data:
        out.append(
            aws_sdk_glue.types.column_statistics_error.deserialize_aws_json_1_1(item)
        )
    return out
