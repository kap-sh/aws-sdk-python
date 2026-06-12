"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#DeleteReportDefinitionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.report_id


class DeleteReportDefinitionResult(TypedDict):
    report_id: NotRequired["aws_sdk_applicationcostprofiler.types.report_id.ReportId"]
    """<p>ID of the report that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReportDefinitionResult) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> DeleteReportDefinitionResult:
    out: DeleteReportDefinitionResult = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
