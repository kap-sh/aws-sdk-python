"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.workflow_definition_name
    import aws_sdk_nova_act.types.workflow_description
    import aws_sdk_nova_act.types.workflow_export_config


class CreateWorkflowDefinitionRequest(TypedDict):
    name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    """<p>The name of the workflow definition. Must be unique within your account and region.</p>"""
    description: NotRequired[
        "aws_sdk_nova_act.types.workflow_description.WorkflowDescription"
    ]
    """<p>An optional description of the workflow definition's purpose and functionality.</p>"""
    export_config: NotRequired[
        "aws_sdk_nova_act.types.workflow_export_config.WorkflowExportConfig"
    ]
    """<p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>"""
    client_token: NotRequired["aws_sdk_nova_act.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowDefinitionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "export_config" in value:
        import aws_sdk_nova_act.types.workflow_export_config

        out["exportConfig"] = (
            aws_sdk_nova_act.types.workflow_export_config.serialize_json(
                value["export_config"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowDefinitionRequest:
    out: CreateWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkflowDefinitionRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "exportConfig" in data:
        import aws_sdk_nova_act.types.workflow_export_config

        out["export_config"] = (
            aws_sdk_nova_act.types.workflow_export_config.deserialize_json(
                data["exportConfig"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
