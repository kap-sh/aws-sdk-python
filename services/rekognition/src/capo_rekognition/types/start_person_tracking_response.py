"""Generated from Smithy shape ``com.amazonaws.rekognition#StartPersonTrackingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id


class StartPersonTrackingResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_rekognition.types.job_id.JobId"]
    """<p>The identifier for the person detection job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetPersonTracking</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPersonTrackingResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPersonTrackingResponse:
    out: StartPersonTrackingResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
