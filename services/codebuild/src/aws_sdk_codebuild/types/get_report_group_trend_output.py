"""Generated from Smithy shape ``com.amazonaws.codebuild#GetReportGroupTrendOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_group_trend_raw_data_list
    import aws_sdk_codebuild.types.report_group_trend_stats


class GetReportGroupTrendOutput(TypedDict, closed=True):
    stats: NotRequired[
        "aws_sdk_codebuild.types.report_group_trend_stats.ReportGroupTrendStats"
    ]
    """<p>Contains the accumulated trend data.</p>"""
    raw_data: NotRequired[
        "aws_sdk_codebuild.types.report_group_trend_raw_data_list.ReportGroupTrendRawDataList"
    ]
    """<p>An array that contains the raw data for each report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReportGroupTrendOutput) -> dict:
    out: dict = {}
    if "stats" in value:
        import aws_sdk_codebuild.types.report_group_trend_stats

        out["stats"] = (
            aws_sdk_codebuild.types.report_group_trend_stats.serialize_aws_json_1_1(
                value["stats"]
            )
        )
    if "raw_data" in value:
        import aws_sdk_codebuild.types.report_group_trend_raw_data_list

        out["rawData"] = (
            aws_sdk_codebuild.types.report_group_trend_raw_data_list.serialize_aws_json_1_1(
                value["raw_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReportGroupTrendOutput:
    out: GetReportGroupTrendOutput = {}  # type: ignore[typeddict-item]
    if "stats" in data:
        import aws_sdk_codebuild.types.report_group_trend_stats

        out["stats"] = (
            aws_sdk_codebuild.types.report_group_trend_stats.deserialize_aws_json_1_1(
                data["stats"]
            )
        )
    if "rawData" in data:
        import aws_sdk_codebuild.types.report_group_trend_raw_data_list

        out["raw_data"] = (
            aws_sdk_codebuild.types.report_group_trend_raw_data_list.deserialize_aws_json_1_1(
                data["rawData"]
            )
        )
    return out
