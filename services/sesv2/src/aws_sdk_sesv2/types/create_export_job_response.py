"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.job_id


class CreateExportJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_sesv2.types.job_id.JobId"]
    """<p>A string that represents the export job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateExportJobResponse:
    out: CreateExportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
