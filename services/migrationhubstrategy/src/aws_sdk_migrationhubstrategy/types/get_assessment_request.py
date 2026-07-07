"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.async_task_id


class GetAssessmentRequest(TypedDict, closed=True):
    id: "aws_sdk_migrationhubstrategy.types.async_task_id.AsyncTaskId"
    """<p> The <code>assessmentid</code> returned by <a>StartAssessment</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssessmentRequest:
    out: GetAssessmentRequest = {}  # type: ignore[typeddict-item]
    return out
