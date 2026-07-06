"""Generated from Smithy shape ``com.amazonaws.inspector2#GetSbomExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.report_id


class GetSbomExportRequest(TypedDict, closed=True):
    report_id: "aws_sdk_inspector2.types.report_id.ReportId"
    """<p>The report ID of the SBOM export to get details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSbomExportRequest) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> GetSbomExportRequest:
    out: GetSbomExportRequest = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    else:
        raise DeserializationError("GetSbomExportRequest.report_id required")
    return out
