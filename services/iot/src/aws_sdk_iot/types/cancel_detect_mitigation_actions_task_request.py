"""Generated from Smithy shape ``com.amazonaws.iot#CancelDetectMitigationActionsTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_actions_task_id


class CancelDetectMitigationActionsTaskRequest(TypedDict, closed=True):
    task_id: "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p> The unique identifier of the task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDetectMitigationActionsTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelDetectMitigationActionsTaskRequest:
    out: CancelDetectMitigationActionsTaskRequest = {}  # type: ignore[typeddict-item]
    return out
