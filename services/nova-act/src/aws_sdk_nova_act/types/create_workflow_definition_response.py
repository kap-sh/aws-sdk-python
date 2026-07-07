"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.workflow_definition_status


class CreateWorkflowDefinitionResponse(TypedDict, closed=True):
    status: "aws_sdk_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The current status of the workflow definition after creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowDefinitionResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.workflow_definition_status

    out["status"] = aws_sdk_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateWorkflowDefinitionResponse:
    out: CreateWorkflowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_definition_status

        out["status"] = (
            aws_sdk_nova_act.types.workflow_definition_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateWorkflowDefinitionResponse.status required")
    return out
