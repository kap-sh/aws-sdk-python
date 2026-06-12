"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditMitigationActionsTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_actions_task_status
    import aws_sdk_iot.types.audit_task_id
    import aws_sdk_iot.types.finding_id
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.timestamp


class ListAuditMitigationActionsTasksRequest(TypedDict):
    audit_task_id: NotRequired["aws_sdk_iot.types.audit_task_id.AuditTaskId"]
    """<p>Specify this filter to limit results to tasks that were applied to results for a specific audit.</p>"""
    finding_id: NotRequired["aws_sdk_iot.types.finding_id.FindingId"]
    """<p>Specify this filter to limit results to tasks that were applied to a specific audit finding.</p>"""
    task_status: NotRequired[
        "aws_sdk_iot.types.audit_mitigation_actions_task_status.AuditMitigationActionsTaskStatus"
    ]
    """<p>Specify this filter to limit results to tasks that are in a specific state.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    start_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p>Specify this filter to limit results to tasks that began on or after a specific date and time.</p>"""
    end_time: "aws_sdk_iot.types.timestamp.Timestamp"
    """<p>Specify this filter to limit results to tasks that were completed or canceled on or before a specific date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditMitigationActionsTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAuditMitigationActionsTasksRequest:
    out: ListAuditMitigationActionsTasksRequest = {}  # type: ignore[typeddict-item]
    return out
