"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditMitigationActionsTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_actions_task_id


class DescribeAuditMitigationActionsTaskRequest(TypedDict):
    task_id: "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p>The unique identifier for the audit mitigation task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditMitigationActionsTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuditMitigationActionsTaskRequest:
    out: DescribeAuditMitigationActionsTaskRequest = {}  # type: ignore[typeddict-item]
    return out
