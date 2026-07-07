"""Generated from Smithy shape ``com.amazonaws.iot#CancelAuditMitigationActionsTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_actions_task_id


class CancelAuditMitigationActionsTaskRequest(TypedDict, closed=True):
    task_id: "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p>The unique identifier for the task that you want to cancel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelAuditMitigationActionsTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelAuditMitigationActionsTaskRequest:
    out: CancelAuditMitigationActionsTaskRequest = {}  # type: ignore[typeddict-item]
    return out
