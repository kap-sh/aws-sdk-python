"""Generated from Smithy shape ``com.amazonaws.rekognition#StartLabelDetectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.job_id


class StartLabelDetectionResponse(TypedDict):
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>The identifier for the label detection job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetLabelDetection</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLabelDetectionResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLabelDetectionResponse:
    out: StartLabelDetectionResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
