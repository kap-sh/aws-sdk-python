"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopSNOMEDCTInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopSNOMEDCTInferenceJobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehendmedical.types.job_id.JobId"]
    """<p> The identifier generated for the job. To get the status of job, use this identifier with the DescribeSNOMEDCTInferenceJob operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSNOMEDCTInferenceJobResponse:
    out: StopSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
