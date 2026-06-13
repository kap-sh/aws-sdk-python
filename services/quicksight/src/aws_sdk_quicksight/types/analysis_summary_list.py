"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_summary

AnalysisSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.analysis_summary.AnalysisSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSummaryList) -> list:
    import aws_sdk_quicksight.types.analysis_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.analysis_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisSummaryList:
    import aws_sdk_quicksight.types.analysis_summary

    out: AnalysisSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.analysis_summary.deserialize_json(item))
    return out
