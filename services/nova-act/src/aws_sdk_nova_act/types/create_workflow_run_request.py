"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.client_info
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.cloud_watch_log_group_name
    import aws_sdk_nova_act.types.model_id
    import aws_sdk_nova_act.types.workflow_definition_name


class CreateWorkflowRunRequest(TypedDict):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition to execute.</p>"""
    model_id: "aws_sdk_nova_act.types.model_id.ModelId"
    """<p>The ID of the AI model to use for workflow execution.</p>"""
    client_token: NotRequired["aws_sdk_nova_act.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>The CloudWatch log group name for storing workflow execution logs.</p>"""
    client_info: "aws_sdk_nova_act.types.client_info.ClientInfo"
    """<p>Information about the client making the request, including compatibility version and SDK version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowRunRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    import aws_sdk_nova_act.types.client_info

    out["clientInfo"] = aws_sdk_nova_act.types.client_info.serialize_json(
        value["client_info"]
    )
    return out


def deserialize_json(data: dict) -> CreateWorkflowRunRequest:
    out: CreateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("CreateWorkflowRunRequest.model_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "clientInfo" in data:
        import aws_sdk_nova_act.types.client_info

        out["client_info"] = aws_sdk_nova_act.types.client_info.deserialize_json(
            data["clientInfo"]
        )
    else:
        raise DeserializationError("CreateWorkflowRunRequest.client_info required")
    return out
