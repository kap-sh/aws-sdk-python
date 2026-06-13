"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FunctionInvocationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_invocation_type
    import aws_sdk_bedrock_agent_runtime.types.function_parameters
    import aws_sdk_bedrock_agent_runtime.types.name


class FunctionInvocationInput(TypedDict):
    action_group: "str"
    """<p>The action group that the function belongs to.</p>"""
    parameters: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.function_parameters.FunctionParameters"
    ]
    """<p>A list of parameters of the function.</p>"""
    function: NotRequired["str"]
    """<p>The name of the function.</p>"""
    action_invocation_type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.action_invocation_type.ActionInvocationType"
    ]
    """<p>Contains information about the function to invoke,</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""
    collaborator_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.name.Name"]
    """<p>The collaborator's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionInvocationInput) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "parameters" in value:
        import aws_sdk_bedrock_agent_runtime.types.function_parameters

        out["parameters"] = (
            aws_sdk_bedrock_agent_runtime.types.function_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "function" in value:
        out["function"] = value["function"]
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


def deserialize_json(data: dict) -> FunctionInvocationInput:
    out: FunctionInvocationInput = {}  # type: ignore[typeddict-item]
    if "actionGroup" in data:
        out["action_group"] = data["actionGroup"]
    else:
        raise DeserializationError("FunctionInvocationInput.action_group required")
    if "parameters" in data:
        import aws_sdk_bedrock_agent_runtime.types.function_parameters

        out["parameters"] = (
            aws_sdk_bedrock_agent_runtime.types.function_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if "function" in data:
        out["function"] = data["function"]
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
