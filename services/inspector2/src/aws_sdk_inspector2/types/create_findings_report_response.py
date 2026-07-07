"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFindingsReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.report_id


class CreateFindingsReportResponse(TypedDict, closed=True):
    report_id: NotRequired["aws_sdk_inspector2.types.report_id.ReportId"]
    """<p>The ID of the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFindingsReportResponse) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> CreateFindingsReportResponse:
    out: CreateFindingsReportResponse = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
