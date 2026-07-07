"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribePiiEntitiesDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.job_id


class DescribePiiEntitiesDetectionJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_comprehend.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePiiEntitiesDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePiiEntitiesDetectionJobRequest:
    out: DescribePiiEntitiesDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "DescribePiiEntitiesDetectionJobRequest.job_id required"
        )
    return out
