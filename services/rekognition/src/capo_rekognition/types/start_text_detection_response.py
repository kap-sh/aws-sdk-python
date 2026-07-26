"""Generated from Smithy shape ``com.amazonaws.rekognition#StartTextDetectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id


class StartTextDetectionResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_rekognition.types.job_id.JobId"]
    """<p>Identifier for the text detection job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetTextDetection</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTextDetectionResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTextDetectionResponse:
    out: StartTextDetectionResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
