"""Generated from Smithy shape ``com.amazonaws.frauddetector#CancelBatchPredictionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class CancelBatchPredictionJobRequest(TypedDict):
    job_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the batch prediction job to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelBatchPredictionJobRequest) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelBatchPredictionJobRequest:
    out: CancelBatchPredictionJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("CancelBatchPredictionJobRequest.job_id required")
    return out
