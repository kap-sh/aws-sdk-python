"""Generated from Smithy shape ``com.amazonaws.iam#GetCredentialReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.report_content_type
    import aws_sdk_iam.types.report_format_type


class GetCredentialReportResponse(TypedDict):
    content: NotRequired["aws_sdk_iam.types.report_content_type.ReportContentType"]
    """<p>Contains the credential report. The report is Base64-encoded.</p>"""
    report_format: NotRequired["aws_sdk_iam.types.report_format_type.ReportFormatType"]
    """<p>The format (MIME type) of the credential report.</p>"""
    generated_time: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    r"""<p> The date and time when the credential report was created, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCredentialReportResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "content" in value:
        import aws_sdk_iam.types.report_content_type

        aws_sdk_iam.types.report_content_type.serialize_query(
            value["content"], pairs, f"{prefix}.Content"
        )
    if "report_format" in value:
        import aws_sdk_iam.types.report_format_type

        aws_sdk_iam.types.report_format_type.serialize_query(
            value["report_format"], pairs, f"{prefix}.ReportFormat"
        )
    if "generated_time" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["generated_time"], pairs, f"{prefix}.GeneratedTime"
        )


def deserialize_query(el: Element) -> GetCredentialReportResponse:
    out: GetCredentialReportResponse = {}  # type: ignore[typeddict-item]
    child_content = el.find("Content")
    if child_content is not None:
        import aws_sdk_iam.types.report_content_type

        out["content"] = aws_sdk_iam.types.report_content_type.deserialize_query(
            child_content
        )
    child_report_format = el.find("ReportFormat")
    if child_report_format is not None:
        import aws_sdk_iam.types.report_format_type

        out["report_format"] = aws_sdk_iam.types.report_format_type.deserialize_query(
            child_report_format
        )
    child_generated_time = el.find("GeneratedTime")
    if child_generated_time is not None:
        import aws_sdk_iam.types.date_type

        out["generated_time"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_generated_time
        )
    return out
