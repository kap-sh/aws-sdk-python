"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.workflow_definition_status


class DeleteWorkflowDefinitionResponse(TypedDict, closed=True):
    status: "aws_sdk_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The status of the workflow definition after deletion request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowDefinitionResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.workflow_definition_status

    out["status"] = aws_sdk_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteWorkflowDefinitionResponse:
    out: DeleteWorkflowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_definition_status

        out["status"] = (
            aws_sdk_nova_act.types.workflow_definition_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteWorkflowDefinitionResponse.status required")
    return out
