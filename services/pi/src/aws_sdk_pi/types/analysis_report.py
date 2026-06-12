"""Generated from Smithy shape ``com.amazonaws.pi#AnalysisReport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_report_id
    import aws_sdk_pi.types.analysis_status
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.insight_list
    import aws_sdk_pi.types.iso_timestamp
    import aws_sdk_pi.types.service_type


class AnalysisReport(TypedDict):
    analysis_report_id: "aws_sdk_pi.types.analysis_report_id.AnalysisReportId"
    """<p>The name of the analysis report.</p>"""
    identifier: NotRequired["aws_sdk_pi.types.identifier_string.IdentifierString"]
    """<p>The unique identifier of the analysis report.</p>"""
    service_type: NotRequired["aws_sdk_pi.types.service_type.ServiceType"]
    """<p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid values are as follows:</p> <ul> <li> <p> <code>RDS</code> </p> </li> <li> <p> <code>DOCDB</code> </p> </li> </ul>"""
    create_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The time you created the analysis report.</p>"""
    start_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The analysis start time in the report.</p>"""
    end_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The analysis end time in the report.</p>"""
    status: NotRequired["aws_sdk_pi.types.analysis_status.AnalysisStatus"]
    """<p>The status of the created analysis report.</p>"""
    insights: NotRequired["aws_sdk_pi.types.insight_list.InsightList"]
    """<p>The list of identified insights in the analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisReport) -> dict:
    out: dict = {}
    out["AnalysisReportId"] = value["analysis_report_id"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "service_type" in value:
        import aws_sdk_pi.types.service_type

        out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
            value["service_type"]
        )
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
    if "insights" in value:
        import aws_sdk_pi.types.insight_list

        out["Insights"] = aws_sdk_pi.types.insight_list.serialize_aws_json_1_1(
            value["insights"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisReport:
    out: AnalysisReport = {}  # type: ignore[typeddict-item]
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        raise DeserializationError("AnalysisReport.analysis_report_id required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
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
    if "Insights" in data:
        import aws_sdk_pi.types.insight_list

        out["insights"] = aws_sdk_pi.types.insight_list.deserialize_aws_json_1_1(
            data["Insights"]
        )
    return out
