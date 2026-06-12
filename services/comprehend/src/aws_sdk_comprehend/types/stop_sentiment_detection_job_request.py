"""Generated from Smithy shape ``com.amazonaws.comprehend#StopSentimentDetectionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id


class StopSentimentDetectionJobRequest(TypedDict):
    job_id: "aws_sdk_comprehend.types.job_id.JobId"
    """<p>The identifier of the sentiment detection job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSentimentDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSentimentDetectionJobRequest:
    out: StopSentimentDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopSentimentDetectionJobRequest.job_id required")
    return out
