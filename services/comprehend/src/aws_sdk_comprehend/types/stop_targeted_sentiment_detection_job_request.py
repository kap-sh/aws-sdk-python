"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTargetedSentimentDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id


class StopTargetedSentimentDetectionJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_comprehend.types.job_id.JobId"
    """<p>The identifier of the targeted sentiment detection job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTargetedSentimentDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTargetedSentimentDetectionJobRequest:
    out: StopTargetedSentimentDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "StopTargetedSentimentDetectionJobRequest.job_id required"
        )
    return out
