"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.analysis_summary

AnalysisSummaryList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.analysis_summary.AnalysisSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisSummaryList) -> list:
    import aws_sdk_cost_explorer.types.analysis_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.analysis_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AnalysisSummaryList:
    import aws_sdk_cost_explorer.types.analysis_summary

    out: AnalysisSummaryList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.analysis_summary.deserialize_aws_json_1_1(item)
        )
    return out
