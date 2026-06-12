"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name


class DeleteWorkflowRunRequest(TypedDict):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the workflow run.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRunRequest:
    out: DeleteWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    return out
