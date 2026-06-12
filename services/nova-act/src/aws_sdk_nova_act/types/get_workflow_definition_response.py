"""Generated from Smithy shape ``com.amazonaws.novaact#GetWorkflowDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.date_timestamp
    import aws_sdk_nova_act.types.workflow_definition_arn
    import aws_sdk_nova_act.types.workflow_definition_name
    import aws_sdk_nova_act.types.workflow_definition_status
    import aws_sdk_nova_act.types.workflow_description
    import aws_sdk_nova_act.types.workflow_export_config


class GetWorkflowDefinitionResponse(TypedDict):
    name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    """<p>The name of the workflow definition.</p>"""
    arn: "aws_sdk_nova_act.types.workflow_definition_arn.WorkflowDefinitionArn"
    """<p>The Amazon Resource Name (ARN) of the workflow definition.</p>"""
    created_at: "aws_sdk_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the workflow definition was created.</p>"""
    description: NotRequired[
        "aws_sdk_nova_act.types.workflow_description.WorkflowDescription"
    ]
    """<p>The description of the workflow definition.</p>"""
    export_config: NotRequired[
        "aws_sdk_nova_act.types.workflow_export_config.WorkflowExportConfig"
    ]
    """<p>The export configuration for the workflow definition.</p>"""
    status: "aws_sdk_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The current status of the workflow definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowDefinitionResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_nova_act.types.date_timestamp

    out["createdAt"] = aws_sdk_nova_act.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "export_config" in value:
        import aws_sdk_nova_act.types.workflow_export_config

        out["exportConfig"] = (
            aws_sdk_nova_act.types.workflow_export_config.serialize_json(
                value["export_config"]
            )
        )
    import aws_sdk_nova_act.types.workflow_definition_status

    out["status"] = aws_sdk_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GetWorkflowDefinitionResponse:
    out: GetWorkflowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.arn required")
    if "createdAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["created_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.created_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "exportConfig" in data:
        import aws_sdk_nova_act.types.workflow_export_config

        out["export_config"] = (
            aws_sdk_nova_act.types.workflow_export_config.deserialize_json(
                data["exportConfig"]
            )
        )
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_definition_status

        out["status"] = (
            aws_sdk_nova_act.types.workflow_definition_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.status required")
    return out
