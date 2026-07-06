"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateUploadJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.uuid


class CreateUploadJobResponse(TypedDict, closed=True):
    job_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier for the created upload job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateUploadJobResponse:
    out: CreateUploadJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CreateUploadJobResponse.job_id required")
    return out
