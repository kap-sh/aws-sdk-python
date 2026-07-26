"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataSourceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.data_source_filter

DataSourceFilters: TypeAlias = list[
    "capo_cloudwatch_logs.types.data_source_filter.DataSourceFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceFilters) -> list:
    import capo_cloudwatch_logs.types.data_source_filter

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.data_source_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceFilters:
    import capo_cloudwatch_logs.types.data_source_filter

    out: DataSourceFilters = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.data_source_filter.deserialize_aws_json_1_1(item)
        )
    return out
