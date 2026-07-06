"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiInvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_invocation_type
    import aws_sdk_bedrock_agent_runtime.types.api_parameters
    import aws_sdk_bedrock_agent_runtime.types.api_path
    import aws_sdk_bedrock_agent_runtime.types.api_request_body
    import aws_sdk_bedrock_agent_runtime.types.name


class ApiInvocationInput(TypedDict, closed=True):
    action_group: "str"
    """<p>The action group that the API operation belongs to.</p>"""
    http_method: NotRequired["str"]
    """<p>The HTTP method of the API operation.</p>"""
    api_path: NotRequired["aws_sdk_bedrock_agent_runtime.types.api_path.ApiPath"]
    """<p>The path to the API operation.</p>"""
    parameters: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.api_parameters.ApiParameters"
    ]
    """<p>The parameters to provide for the API request, as the agent elicited from the user.</p>"""
    request_body: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.api_request_body.ApiRequestBody"
    ]
    """<p>The request body to provide for the API request, as the agent elicited from the user.</p>"""
    action_invocation_type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.action_invocation_type.ActionInvocationType"
    ]
    """<p>Contains information about the API operation to invoke.</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""
    collaborator_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.name.Name"]
    """<p>The agent collaborator's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiInvocationInput) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "api_path" in value:
        out["apiPath"] = value["api_path"]
    if "parameters" in value:
        import aws_sdk_bedrock_agent_runtime.types.api_parameters

        out["parameters"] = (
            aws_sdk_bedrock_agent_runtime.types.api_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "request_body" in value:
        import aws_sdk_bedrock_agent_runtime.types.api_request_body

        out["requestBody"] = (
            aws_sdk_bedrock_agent_runtime.types.api_request_body.serialize_json(
                value["request_body"]
            )
        )
    if "action_invocation_type" in value:
        import aws_sdk_bedrock_agent_runtime.types.action_invocation_type

        out["actionInvocationType"] = (
            aws_sdk_bedrock_agent_runtime.types.action_invocation_type.serialize_json(
                value["action_invocation_type"]
            )
        )
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "collaborator_name" in value:
        out["collaboratorName"] = value["collaborator_name"]
    return out


def deserialize_json(data: dict) -> ApiInvocationInput:
    out: ApiInvocationInput = {}  # type: ignore[typeddict-item]
    if "actionGroup" in data:
        out["action_group"] = data["actionGroup"]
    else:
        raise DeserializationError("ApiInvocationInput.action_group required")
    if "httpMethod" in data:
        out["http_method"] = data["httpMethod"]
    if "apiPath" in data:
        out["api_path"] = data["apiPath"]
    if "parameters" in data:
        import aws_sdk_bedrock_agent_runtime.types.api_parameters

        out["parameters"] = (
            aws_sdk_bedrock_agent_runtime.types.api_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if "requestBody" in data:
        import aws_sdk_bedrock_agent_runtime.types.api_request_body

        out["request_body"] = (
            aws_sdk_bedrock_agent_runtime.types.api_request_body.deserialize_json(
                data["requestBody"]
            )
        )
    if "actionInvocationType" in data:
        import aws_sdk_bedrock_agent_runtime.types.action_invocation_type

        out["action_invocation_type"] = (
            aws_sdk_bedrock_agent_runtime.types.action_invocation_type.deserialize_json(
                data["actionInvocationType"]
            )
        )
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    return out
