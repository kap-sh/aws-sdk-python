"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_status
    import aws_sdk_pi.types.iso_timestamp
    import aws_sdk_pi.types.string
    import aws_sdk_pi.types.tag_list


class AnalysisReportSummary(TypedDict, closed=True):
    analysis_report_id: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The name of the analysis report.</p>"""
    create_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The time you created the analysis report.</p>"""
    start_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time of the analysis in the report.</p>"""
    end_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time of the analysis in the report.</p>"""
    status: NotRequired["aws_sdk_pi.types.analysis_status.AnalysisStatus"]
    """<p>The status of the analysis report.</p>"""
    tags: NotRequired["aws_sdk_pi.types.tag_list.TagList"]
    """<p>List of all the tags added to the analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisReportSummary) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    if "create_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["CreateTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "start_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["StartTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["EndTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import aws_sdk_pi.types.analysis_status

        out["Status"] = aws_sdk_pi.types.analysis_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_pi.types.tag_list

        out["Tags"] = aws_sdk_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisReportSummary:
    out: AnalysisReportSummary = {}  # type: ignore[typeddict-item]
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    if "CreateTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["create_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "StartTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["start_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["end_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Status" in data:
        import aws_sdk_pi.types.analysis_status

        out["status"] = aws_sdk_pi.types.analysis_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Tags" in data:
        import aws_sdk_pi.types.tag_list

        out["tags"] = aws_sdk_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
