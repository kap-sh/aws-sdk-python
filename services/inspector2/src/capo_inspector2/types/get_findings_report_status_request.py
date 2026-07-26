"""Generated from Smithy shape ``com.amazonaws.inspector2#GetFindingsReportStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.report_id


class GetFindingsReportStatusRequest(TypedDict, closed=True):
    report_id: NotRequired["capo_inspector2.types.report_id.ReportId"]
    """<p>The ID of the report to retrieve the status of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsReportStatusRequest) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> GetFindingsReportStatusRequest:
    out: GetFindingsReportStatusRequest = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
