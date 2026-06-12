"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopRxNormInferenceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopRxNormInferenceJobRequest(TypedDict):
    job_id: "aws_sdk_comprehendmedical.types.job_id.JobId"
    """<p>The identifier of the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRxNormInferenceJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRxNormInferenceJobRequest:
    out: StopRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopRxNormInferenceJobRequest.job_id required")
    return out
