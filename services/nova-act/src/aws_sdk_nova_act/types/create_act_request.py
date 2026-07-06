"""Generated from Smithy shape ``com.amazonaws.novaact#CreateActRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.task
    import aws_sdk_nova_act.types.tool_specs
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name


class CreateActRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the session.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the session.</p>"""
    session_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session to create the act in.</p>"""
    task: "aws_sdk_nova_act.types.task.Task"
    """<p>The task description that defines what the act should accomplish.</p>"""
    tool_specs: NotRequired["aws_sdk_nova_act.types.tool_specs.ToolSpecs"]
    """<p>A list of tool specifications that the act can invoke to complete its task.</p>"""
    client_token: NotRequired["aws_sdk_nova_act.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActRequest) -> dict:
    out: dict = {}
    out["task"] = value["task"]
    if "tool_specs" in value:
        import aws_sdk_nova_act.types.tool_specs

        out["toolSpecs"] = aws_sdk_nova_act.types.tool_specs.serialize_json(
            value["tool_specs"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateActRequest:
    out: CreateActRequest = {}  # type: ignore[typeddict-item]
    if "task" in data:
        out["task"] = data["task"]
    else:
        raise DeserializationError("CreateActRequest.task required")
    if "toolSpecs" in data:
        import aws_sdk_nova_act.types.tool_specs

        out["tool_specs"] = aws_sdk_nova_act.types.tool_specs.deserialize_json(
            data["toolSpecs"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
