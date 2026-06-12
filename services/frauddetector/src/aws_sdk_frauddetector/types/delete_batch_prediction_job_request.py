"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteBatchPredictionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class DeleteBatchPredictionJobRequest(TypedDict):
    job_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the batch prediction job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBatchPredictionJobRequest) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBatchPredictionJobRequest:
    out: DeleteBatchPredictionJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DeleteBatchPredictionJobRequest.job_id required")
    return out
