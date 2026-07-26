"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateSbomExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.report_id


class CreateSbomExportResponse(TypedDict, closed=True):
    report_id: NotRequired["capo_inspector2.types.report_id.ReportId"]
    """<p>The report ID for the software bill of materials (SBOM) report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSbomExportResponse) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> CreateSbomExportResponse:
    out: CreateSbomExportResponse = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    return out
