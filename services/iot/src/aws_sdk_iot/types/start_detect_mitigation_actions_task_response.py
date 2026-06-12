"""Generated from Smithy shape ``com.amazonaws.iot#StartDetectMitigationActionsTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_actions_task_id


class StartDetectMitigationActionsTaskResponse(TypedDict):
    task_id: NotRequired[
        "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p> The unique identifier of the task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDetectMitigationActionsTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> StartDetectMitigationActionsTaskResponse:
    out: StartDetectMitigationActionsTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
