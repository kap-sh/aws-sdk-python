"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_task_id


class DescribeAuditTaskRequest(TypedDict, closed=True):
    task_id: "capo_iot.types.audit_task_id.AuditTaskId"
    """<p>The ID of the audit whose information you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuditTaskRequest:
    out: DescribeAuditTaskRequest = {}  # type: ignore[typeddict-item]
    return out
