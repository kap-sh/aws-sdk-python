"""Generated from Smithy shape ``com.amazonaws.novaact#UpdateWorkflowRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name
    import aws_sdk_nova_act.types.workflow_run_status


class UpdateWorkflowRunRequest(TypedDict):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the workflow run.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run to update.</p>"""
    status: "aws_sdk_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The new status to set for the workflow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowRunRequest) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.workflow_run_status

    out["status"] = aws_sdk_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkflowRunRequest:
    out: UpdateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_run_status

        out["status"] = aws_sdk_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateWorkflowRunRequest.status required")
    return out
