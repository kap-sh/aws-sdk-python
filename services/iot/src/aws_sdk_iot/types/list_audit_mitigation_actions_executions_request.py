"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditMitigationActionsExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_actions_execution_status
    import aws_sdk_iot.types.finding_id
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.mitigation_actions_task_id
    import aws_sdk_iot.types.next_token


class ListAuditMitigationActionsExecutionsRequest(TypedDict):
    task_id: "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p>Specify this filter to limit results to actions for a specific audit mitigation actions task.</p>"""
    action_status: NotRequired[
        "aws_sdk_iot.types.audit_mitigation_actions_execution_status.AuditMitigationActionsExecutionStatus"
    ]
    """<p>Specify this filter to limit results to those with a specific status.</p>"""
    finding_id: "aws_sdk_iot.types.finding_id.FindingId"
    """<p>Specify this filter to limit results to those that were applied to a specific audit finding.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditMitigationActionsExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAuditMitigationActionsExecutionsRequest:
    out: ListAuditMitigationActionsExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
