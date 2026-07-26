"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.date_timestamp
    import capo_nova_act.types.workflow_definition_arn
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_definition_status


class WorkflowDefinitionSummary(TypedDict, closed=True):
    workflow_definition_arn: (
        "capo_nova_act.types.workflow_definition_arn.WorkflowDefinitionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the workflow definition.</p>"""
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition.</p>"""
    created_at: "capo_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the workflow definition was created.</p>"""
    status: "capo_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The current status of the workflow definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowDefinitionSummary) -> dict:
    out: dict = {}
    out["workflowDefinitionArn"] = value["workflow_definition_arn"]
    out["workflowDefinitionName"] = value["workflow_definition_name"]
    import capo_nova_act.types.date_timestamp

    out["createdAt"] = capo_nova_act.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_nova_act.types.workflow_definition_status

    out["status"] = capo_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> WorkflowDefinitionSummary:
    out: WorkflowDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "workflowDefinitionArn" in data:
        out["workflow_definition_arn"] = data["workflowDefinitionArn"]
    else:
        raise DeserializationError(
            "WorkflowDefinitionSummary.workflow_definition_arn required"
        )
    if "workflowDefinitionName" in data:
        out["workflow_definition_name"] = data["workflowDefinitionName"]
    else:
        raise DeserializationError(
            "WorkflowDefinitionSummary.workflow_definition_name required"
        )
    if "createdAt" in data:
        import capo_nova_act.types.date_timestamp

        out["created_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("WorkflowDefinitionSummary.created_at required")
    if "status" in data:
        import capo_nova_act.types.workflow_definition_status

        out["status"] = capo_nova_act.types.workflow_definition_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("WorkflowDefinitionSummary.status required")
    return out
