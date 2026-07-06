"""Generated from Smithy shape ``com.amazonaws.inspector#GetAssessmentReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.report_status
    import aws_sdk_inspector.types.url


class GetAssessmentReportResponse(TypedDict, closed=True):
    status: "aws_sdk_inspector.types.report_status.ReportStatus"
    """<p>Specifies the status of the request to generate an assessment report. </p>"""
    url: NotRequired["aws_sdk_inspector.types.url.Url"]
    """<p>Specifies the URL where you can find the generated assessment report. This parameter is only returned if the report is successfully generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssessmentReportResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.report_status

    out["status"] = aws_sdk_inspector.types.report_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssessmentReportResponse:
    out: GetAssessmentReportResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_inspector.types.report_status

        out["status"] = aws_sdk_inspector.types.report_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        raise DeserializationError("GetAssessmentReportResponse.status required")
    if "url" in data:
        out["url"] = data["url"]
    return out
