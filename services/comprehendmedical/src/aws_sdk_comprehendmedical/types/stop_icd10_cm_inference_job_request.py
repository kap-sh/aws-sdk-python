"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopICD10CMInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopICD10CMInferenceJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_comprehendmedical.types.job_id.JobId"
    """<p>The identifier of the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopICD10CMInferenceJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopICD10CMInferenceJobRequest:
    out: StopICD10CMInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopICD10CMInferenceJobRequest.job_id required")
    return out
