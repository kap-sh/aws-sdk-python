"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.data_source_summary

DataSourceSummaryList: TypeAlias = list[
    "capo_kendra.types.data_source_summary.DataSourceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceSummaryList) -> list:
    import capo_kendra.types.data_source_summary

    out: list = []
    for item in value:
        out.append(capo_kendra.types.data_source_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataSourceSummaryList:
    import capo_kendra.types.data_source_summary

    out: DataSourceSummaryList = []
    for item in data:
        out.append(capo_kendra.types.data_source_summary.deserialize_aws_json_1_1(item))
    return out
