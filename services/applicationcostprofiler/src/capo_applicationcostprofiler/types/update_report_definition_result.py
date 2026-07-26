"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#UpdateReportDefinitionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.report_id


class UpdateReportDefinitionResult(TypedDict, closed=True):
    report_id: NotRequired["capo_applicationcostprofiler.types.report_id.ReportId"]
    """<p>ID of the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReportDefinitionResult) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> UpdateReportDefinitionResult:
    out: UpdateReportDefinitionResult = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
