"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.job_id


class CreateImportJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_sesv2.types.job_id.JobId"]
    """<p>A string that represents the import job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImportJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateImportJobResponse:
    out: CreateImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
