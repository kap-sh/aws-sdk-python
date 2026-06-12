"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_task_id


class DescribeAuditTaskRequest(TypedDict):
    task_id: "aws_sdk_iot.types.audit_task_id.AuditTaskId"
    """<p>The ID of the audit whose information you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuditTaskRequest:
    out: DescribeAuditTaskRequest = {}  # type: ignore[typeddict-item]
    return out
