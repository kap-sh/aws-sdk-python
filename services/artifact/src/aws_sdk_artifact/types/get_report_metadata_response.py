"""Generated from Smithy shape ``com.amazonaws.artifact#GetReportMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_artifact.types.report_detail


class GetReportMetadataResponse(TypedDict):
    report_details: NotRequired["aws_sdk_artifact.types.report_detail.ReportDetail"]
    """<p>Report resource detail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportMetadataResponse) -> dict:
    out: dict = {}
    if "report_details" in value:
        import aws_sdk_artifact.types.report_detail

        out["reportDetails"] = aws_sdk_artifact.types.report_detail.serialize_json(
            value["report_details"]
        )
    return out


def deserialize_json(data: dict) -> GetReportMetadataResponse:
    out: GetReportMetadataResponse = {}  # type: ignore[typeddict-item]
    if "reportDetails" in data:
        import aws_sdk_artifact.types.report_detail

        out["report_details"] = aws_sdk_artifact.types.report_detail.deserialize_json(
            data["reportDetails"]
        )
    return out
