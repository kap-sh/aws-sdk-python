"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopICD10CMInferenceJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopICD10CMInferenceJobResponse(TypedDict):
    job_id: NotRequired["aws_sdk_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier generated for the job. To get the status of job, use this identifier with the <code>DescribeICD10CMInferenceJob</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopICD10CMInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopICD10CMInferenceJobResponse:
    out: StopICD10CMInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
