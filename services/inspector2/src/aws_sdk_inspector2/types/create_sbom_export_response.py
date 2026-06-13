"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateSbomExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.report_id


class CreateSbomExportResponse(TypedDict):
    report_id: NotRequired["aws_sdk_inspector2.types.report_id.ReportId"]
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
