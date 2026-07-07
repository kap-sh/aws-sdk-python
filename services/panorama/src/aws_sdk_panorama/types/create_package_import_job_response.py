"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_id


class CreatePackageImportJobResponse(TypedDict, closed=True):
    job_id: "aws_sdk_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreatePackageImportJobResponse:
    out: CreatePackageImportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CreatePackageImportJobResponse.job_id required")
    return out
