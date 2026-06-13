"""Generated from Smithy shape ``com.amazonaws.inspector2#CancelFindingsReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.report_id


class CancelFindingsReportResponse(TypedDict):
    report_id: "aws_sdk_inspector2.types.report_id.ReportId"
    """<p>The ID of the canceled report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelFindingsReportResponse) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> CancelFindingsReportResponse:
    out: CancelFindingsReportResponse = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    else:
        raise DeserializationError("CancelFindingsReportResponse.report_id required")
    return out
