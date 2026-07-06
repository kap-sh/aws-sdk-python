"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FindingsReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.findings_report_id
    import aws_sdk_codeguruprofiler.types.timestamp


class FindingsReportSummary(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_codeguruprofiler.types.findings_report_id.FindingsReportId"
    ]
    """<p>The universally unique identifier (UUID) of the recommendation report.</p>"""
    profiling_group_name: NotRequired["str"]
    """<p>The name of the profiling group that is associated with the analysis data.</p>"""
    profile_start_time: NotRequired[
        "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    ]
    """<p>The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""
    profile_end_time: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    total_number_of_findings: NotRequired["int"]
    """<p>The total number of different recommendations that were found by the analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingsReportSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "profiling_group_name" in value:
        out["profilingGroupName"] = value["profiling_group_name"]
    if "profile_start_time" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profileStartTime"] = (
            aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
                value["profile_start_time"]
            )
        )
    if "profile_end_time" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profileEndTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
            value["profile_end_time"]
        )
    if "total_number_of_findings" in value:
        out["totalNumberOfFindings"] = value["total_number_of_findings"]
    return out


def deserialize_json(data: dict) -> FindingsReportSummary:
    out: FindingsReportSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "profilingGroupName" in data:
        out["profiling_group_name"] = data["profilingGroupName"]
    if "profileStartTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profile_start_time"] = (
            aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileStartTime"]
            )
        )
    if "profileEndTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["profile_end_time"] = (
            aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
                data["profileEndTime"]
            )
        )
    if "totalNumberOfFindings" in data:
        out["total_number_of_findings"] = data["totalNumberOfFindings"]
    return out
