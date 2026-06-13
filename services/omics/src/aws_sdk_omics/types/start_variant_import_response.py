"""Generated from Smithy shape ``com.amazonaws.omics#StartVariantImportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.resource_id


class StartVariantImportResponse(TypedDict):
    job_id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVariantImportResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartVariantImportResponse:
    out: StartVariantImportResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StartVariantImportResponse.job_id required")
    return out
