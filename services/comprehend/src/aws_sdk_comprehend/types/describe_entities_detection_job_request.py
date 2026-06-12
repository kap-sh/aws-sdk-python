"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEntitiesDetectionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id


class DescribeEntitiesDetectionJobRequest(TypedDict):
    job_id: "aws_sdk_comprehend.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend generated for the job. The <code>StartEntitiesDetectionJob</code> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitiesDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitiesDetectionJobRequest:
    out: DescribeEntitiesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "DescribeEntitiesDetectionJobRequest.job_id required"
        )
    return out
