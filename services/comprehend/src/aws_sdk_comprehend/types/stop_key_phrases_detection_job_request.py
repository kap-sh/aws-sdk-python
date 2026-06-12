"""Generated from Smithy shape ``com.amazonaws.comprehend#StopKeyPhrasesDetectionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id


class StopKeyPhrasesDetectionJobRequest(TypedDict):
    job_id: "aws_sdk_comprehend.types.job_id.JobId"
    """<p>The identifier of the key phrases detection job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopKeyPhrasesDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopKeyPhrasesDetectionJobRequest:
    out: StopKeyPhrasesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopKeyPhrasesDetectionJobRequest.job_id required")
    return out
