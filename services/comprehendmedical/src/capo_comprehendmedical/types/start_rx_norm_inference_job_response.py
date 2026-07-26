"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StartRxNormInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class StartRxNormInferenceJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier of the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRxNormInferenceJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRxNormInferenceJobResponse:
    out: StartRxNormInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
