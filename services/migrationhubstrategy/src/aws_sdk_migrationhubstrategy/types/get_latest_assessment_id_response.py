"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetLatestAssessmentIdResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.async_task_id


class GetLatestAssessmentIdResponse(TypedDict):
    id: NotRequired["aws_sdk_migrationhubstrategy.types.async_task_id.AsyncTaskId"]
    """<p>The latest ID for the specific assessment task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLatestAssessmentIdResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GetLatestAssessmentIdResponse:
    out: GetLatestAssessmentIdResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
