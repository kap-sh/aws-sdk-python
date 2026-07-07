"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditMitigationActionsExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list
    import aws_sdk_iot.types.next_token


class ListAuditMitigationActionsExecutionsResponse(TypedDict, closed=True):
    actions_executions: NotRequired[
        "aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list.AuditMitigationActionExecutionMetadataList"
    ]
    """<p>A set of task execution results based on the input parameters. Details include the mitigation action applied, start time, and task status.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditMitigationActionsExecutionsResponse) -> dict:
    out: dict = {}
    if "actions_executions" in value:
        import aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list

        out["actionsExecutions"] = (
            aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list.serialize_json(
                value["actions_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditMitigationActionsExecutionsResponse:
    out: ListAuditMitigationActionsExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "actionsExecutions" in data:
        import aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list

        out["actions_executions"] = (
            aws_sdk_iot.types.audit_mitigation_action_execution_metadata_list.deserialize_json(
                data["actionsExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
