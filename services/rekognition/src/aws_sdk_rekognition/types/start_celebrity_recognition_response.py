"""Generated from Smithy shape ``com.amazonaws.rekognition#StartCelebrityRecognitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.job_id


class StartCelebrityRecognitionResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>The identifier for the celebrity recognition analysis job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetCelebrityRecognition</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCelebrityRecognitionResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCelebrityRecognitionResponse:
    out: StartCelebrityRecognitionResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
