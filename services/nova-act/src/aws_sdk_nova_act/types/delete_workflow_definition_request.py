"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.workflow_definition_name


class DeleteWorkflowDefinitionRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowDefinitionRequest:
    out: DeleteWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
