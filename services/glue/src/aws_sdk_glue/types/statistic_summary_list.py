"""Generated from Smithy shape ``com.amazonaws.glue#StatisticSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.statistic_summary

StatisticSummaryList: TypeAlias = list[
    "aws_sdk_glue.types.statistic_summary.StatisticSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticSummaryList) -> list:
    import aws_sdk_glue.types.statistic_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.statistic_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatisticSummaryList:
    import aws_sdk_glue.types.statistic_summary

    out: StatisticSummaryList = []
    for item in data:
        out.append(aws_sdk_glue.types.statistic_summary.deserialize_aws_json_1_1(item))
    return out
