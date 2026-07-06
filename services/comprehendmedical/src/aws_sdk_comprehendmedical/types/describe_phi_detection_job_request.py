"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribePHIDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class DescribePHIDetectionJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_comprehendmedical.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend Medical generated for the job. The <code>StartPHIDetectionJob</code> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePHIDetectionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePHIDetectionJobRequest:
    out: DescribePHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribePHIDetectionJobRequest.job_id required")
    return out
