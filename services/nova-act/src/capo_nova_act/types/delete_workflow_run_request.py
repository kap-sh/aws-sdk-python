"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name


class DeleteWorkflowRunRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the workflow run.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRunRequest:
    out: DeleteWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    return out
