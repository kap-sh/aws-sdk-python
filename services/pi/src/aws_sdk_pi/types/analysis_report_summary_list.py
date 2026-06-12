"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisReportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_report_summary

AnalysisReportSummaryList: TypeAlias = list[
    "aws_sdk_pi.types.analysis_report_summary.AnalysisReportSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisReportSummaryList) -> list:
    import aws_sdk_pi.types.analysis_report_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pi.types.analysis_report_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AnalysisReportSummaryList:
    import aws_sdk_pi.types.analysis_report_summary

    out: AnalysisReportSummaryList = []
    for item in data:
        out.append(
            aws_sdk_pi.types.analysis_report_summary.deserialize_aws_json_1_1(item)
        )
    return out
