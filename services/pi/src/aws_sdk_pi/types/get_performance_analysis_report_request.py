"""Generated from Smithy shape ``com.amazonaws.pi#GetPerformanceAnalysisReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.accept_language
    import aws_sdk_pi.types.analysis_report_id
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.service_type
    import aws_sdk_pi.types.text_format


class GetPerformanceAnalysisReportRequest(TypedDict, closed=True):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights will return metrics. Valid value is <code>RDS</code>.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as <i>ResourceID</i>. When you call <code>DescribeDBInstances</code>, the identifier is returned as <code>DbiResourceId</code>.</p> <p>To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>.</p>"""
    analysis_report_id: "aws_sdk_pi.types.analysis_report_id.AnalysisReportId"
    """<p>A unique identifier of the created analysis report. For example, <code>report-12345678901234567</code> </p>"""
    text_format: NotRequired["aws_sdk_pi.types.text_format.TextFormat"]
    """<p>Indicates the text format in the report. The options are <code>PLAIN_TEXT</code> or <code>MARKDOWN</code>. The default value is <code>plain text</code>.</p>"""
    accept_language: NotRequired["aws_sdk_pi.types.accept_language.AcceptLanguage"]
    """<p>The text language in the report. The default language is <code>EN_US</code> (English). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPerformanceAnalysisReportRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    out["AnalysisReportId"] = value["analysis_report_id"]
    if "text_format" in value:
        import aws_sdk_pi.types.text_format

        out["TextFormat"] = aws_sdk_pi.types.text_format.serialize_aws_json_1_1(
            value["text_format"]
        )
    if "accept_language" in value:
        import aws_sdk_pi.types.accept_language

        out["AcceptLanguage"] = aws_sdk_pi.types.accept_language.serialize_aws_json_1_1(
            value["accept_language"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPerformanceAnalysisReportRequest:
    out: GetPerformanceAnalysisReportRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError(
            "GetPerformanceAnalysisReportRequest.service_type required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "GetPerformanceAnalysisReportRequest.identifier required"
        )
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        raise DeserializationError(
            "GetPerformanceAnalysisReportRequest.analysis_report_id required"
        )
    if "TextFormat" in data:
        import aws_sdk_pi.types.text_format

        out["text_format"] = aws_sdk_pi.types.text_format.deserialize_aws_json_1_1(
            data["TextFormat"]
        )
    if "AcceptLanguage" in data:
        import aws_sdk_pi.types.accept_language

        out["accept_language"] = (
            aws_sdk_pi.types.accept_language.deserialize_aws_json_1_1(
                data["AcceptLanguage"]
            )
        )
    return out
