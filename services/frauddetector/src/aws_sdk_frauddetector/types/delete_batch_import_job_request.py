"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteBatchImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class DeleteBatchImportJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the batch import job to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBatchImportJobRequest) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBatchImportJobRequest:
    out: DeleteBatchImportJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DeleteBatchImportJobRequest.job_id required")
    return out
