"""Generated from Smithy shape ``com.amazonaws.inspector2#CancelSbomExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.report_id


class CancelSbomExportRequest(TypedDict):
    report_id: "aws_sdk_inspector2.types.report_id.ReportId"
    """<p>The report ID of the SBOM export to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSbomExportRequest) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> CancelSbomExportRequest:
    out: CancelSbomExportRequest = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    else:
        raise DeserializationError("CancelSbomExportRequest.report_id required")
    return out
