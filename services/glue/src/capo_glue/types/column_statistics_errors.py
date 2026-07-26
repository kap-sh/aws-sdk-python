"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_statistics_error

ColumnStatisticsErrors: TypeAlias = list[
    "capo_glue.types.column_statistics_error.ColumnStatisticsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsErrors) -> list:
    import capo_glue.types.column_statistics_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.column_statistics_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnStatisticsErrors:
    import capo_glue.types.column_statistics_error

    out: ColumnStatisticsErrors = []
    for item in data:
        out.append(
            capo_glue.types.column_statistics_error.deserialize_aws_json_1_1(item)
        )
    return out
