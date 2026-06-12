"""Generated from Smithy shape ``com.amazonaws.pi#DeletePerformanceAnalysisReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_report_id
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.service_type


class DeletePerformanceAnalysisReportRequest(TypedDict):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    analysis_report_id: "aws_sdk_pi.types.analysis_report_id.AnalysisReportId"
    """<p>The unique identifier of the analysis report for deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePerformanceAnalysisReportRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePerformanceAnalysisReportRequest:
    out: DeletePerformanceAnalysisReportRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError(
            "DeletePerformanceAnalysisReportRequest.service_type required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "DeletePerformanceAnalysisReportRequest.identifier required"
        )
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        raise DeserializationError(
            "DeletePerformanceAnalysisReportRequest.analysis_report_id required"
        )
    return out
