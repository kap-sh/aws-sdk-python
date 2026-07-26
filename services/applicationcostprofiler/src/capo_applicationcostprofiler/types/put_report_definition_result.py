"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#PutReportDefinitionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.report_id


class PutReportDefinitionResult(TypedDict, closed=True):
    report_id: NotRequired["capo_applicationcostprofiler.types.report_id.ReportId"]
    """<p>ID of the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutReportDefinitionResult) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> PutReportDefinitionResult:
    out: PutReportDefinitionResult = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
