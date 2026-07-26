"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.async_task_id


class StartAssessmentResponse(TypedDict, closed=True):
    assessment_id: NotRequired[
        "capo_migrationhubstrategy.types.async_task_id.AsyncTaskId"
    ]
    """<p> The ID of the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    return out


def deserialize_json(data: dict) -> StartAssessmentResponse:
    out: StartAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    return out
