"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditMitigationActionsTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list
    import aws_sdk_iot.types.next_token


class ListAuditMitigationActionsTasksResponse(TypedDict):
    tasks: NotRequired[
        "aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list.AuditMitigationActionsTaskMetadataList"
    ]
    """<p>The collection of audit mitigation tasks that matched the filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditMitigationActionsTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list

        out["tasks"] = (
            aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list.serialize_json(
                value["tasks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditMitigationActionsTasksResponse:
    out: ListAuditMitigationActionsTasksResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list

        out["tasks"] = (
            aws_sdk_iot.types.audit_mitigation_actions_task_metadata_list.deserialize_json(
                data["tasks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
