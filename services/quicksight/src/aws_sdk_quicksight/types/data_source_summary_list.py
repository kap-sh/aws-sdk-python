"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source_summary

DataSourceSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_source_summary.DataSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummaryList) -> list:
    import aws_sdk_quicksight.types.data_source_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSummaryList:
    import aws_sdk_quicksight.types.data_source_summary

    out: DataSourceSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.data_source_summary.deserialize_json(item))
    return out
