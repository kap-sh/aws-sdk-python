"""Generated from Smithy shape ``com.amazonaws.artifact#GetReportMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.report_detail


class GetReportMetadataResponse(TypedDict, closed=True):
    report_details: NotRequired["capo_artifact.types.report_detail.ReportDetail"]
    """<p>Report resource detail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportMetadataResponse) -> dict:
    out: dict = {}
    if "report_details" in value:
        import capo_artifact.types.report_detail

        out["reportDetails"] = capo_artifact.types.report_detail.serialize_json(
            value["report_details"]
        )
    return out


def deserialize_json(data: dict) -> GetReportMetadataResponse:
    out: GetReportMetadataResponse = {}  # type: ignore[typeddict-item]
    if "reportDetails" in data:
        import capo_artifact.types.report_detail

        out["report_details"] = capo_artifact.types.report_detail.deserialize_json(
            data["reportDetails"]
        )
    return out
