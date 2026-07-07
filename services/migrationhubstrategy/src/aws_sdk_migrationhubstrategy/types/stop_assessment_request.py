"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StopAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.async_task_id


class StopAssessmentRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_migrationhubstrategy.types.async_task_id.AsyncTaskId"
    """<p> The <code>assessmentId</code> returned by <a>StartAssessment</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopAssessmentRequest) -> dict:
    out: dict = {}
    out["assessmentId"] = value["assessment_id"]
    return out


def deserialize_json(data: dict) -> StopAssessmentRequest:
    out: StopAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    else:
        raise DeserializationError("StopAssessmentRequest.assessment_id required")
    return out
