"""Generated from Smithy shape ``com.amazonaws.rekognition#StartSegmentDetectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id


class StartSegmentDetectionResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_rekognition.types.job_id.JobId"]
    """<p>Unique identifier for the segment detection job. The <code>JobId</code> is returned from <code>StartSegmentDetection</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSegmentDetectionResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSegmentDetectionResponse:
    out: StartSegmentDetectionResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
