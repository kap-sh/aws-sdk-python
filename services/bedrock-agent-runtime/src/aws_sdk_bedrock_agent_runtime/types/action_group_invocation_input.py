"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupInvocationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_group_name
    import aws_sdk_bedrock_agent_runtime.types.api_path
    import aws_sdk_bedrock_agent_runtime.types.execution_type
    import aws_sdk_bedrock_agent_runtime.types.function
    import aws_sdk_bedrock_agent_runtime.types.parameters
    import aws_sdk_bedrock_agent_runtime.types.request_body
    import aws_sdk_bedrock_agent_runtime.types.verb

class ActionGroupInvocationInput(TypedDict):
    action_group_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.action_group_name.ActionGroupName"]
    """<p>The name of the action group.</p>"""
    verb: NotRequired["aws_sdk_bedrock_agent_runtime.types.verb.Verb"]
    """<p>The API method being used, based off the action group.</p>"""
    api_path: NotRequired["aws_sdk_bedrock_agent_runtime.types.api_path.ApiPath"]
    """<p>The path to the API to call, based off the action group.</p>"""
    parameters: NotRequired["aws_sdk_bedrock_agent_runtime.types.parameters.Parameters"]
    """<p>The parameters in the Lambda input event.</p>"""
    request_body: NotRequired["aws_sdk_bedrock_agent_runtime.types.request_body.RequestBody"]
    """<p>The parameters in the request body for the Lambda input event.</p>"""
    function: NotRequired["aws_sdk_bedrock_agent_runtime.types.function.Function"]
    """<p>The function in the action group to call.</p>"""
    execution_type: NotRequired["aws_sdk_bedrock_agent_runtime.types.execution_type.ExecutionType"]
    """<p>How fulfillment of the action is handled. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/action-handle.html\">Handling fulfillment of the action</a>.</p>"""
    invocation_id: NotRequired["str"]
    """<p>The unique identifier of the invocation. Only returned if the <code>executionType</code> is <code>RETURN_CONTROL</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupInvocationInput) -> dict:
    out: dict = {}
    if "action_group_name" in value:
        out["actionGroupName"] = value["action_group_name"]
    if "verb" in value:
        out["verb"] = value["verb"]
    if "api_path" in value:
        out["apiPath"] = value["api_path"]
    if "parameters" in value:
        import aws_sdk_bedrock_agent_runtime.types.parameters
        out["parameters"] = aws_sdk_bedrock_agent_runtime.types.parameters.serialize_json(value["parameters"])
    if "request_body" in value:
        import aws_sdk_bedrock_agent_runtime.types.request_body
        out["requestBody"] = aws_sdk_bedrock_agent_runtime.types.request_body.serialize_json(value["request_body"])
    if "function" in value:
        out["function"] = value["function"]
    if "execution_type" in value:
        import aws_sdk_bedrock_agent_runtime.types.execution_type
        out["executionType"] = aws_sdk_bedrock_agent_runtime.types.execution_type.serialize_json(value["execution_type"])
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> ActionGroupInvocationInput:
    out: ActionGroupInvocationInput = {}  # type: ignore[typeddict-item]
    if "actionGroupName" in data:
        out["action_group_name"] = data["actionGroupName"]
    if "verb" in data:
        out["verb"] = data["verb"]
    if "apiPath" in data:
        out["api_path"] = data["apiPath"]
    if "parameters" in data:
        import aws_sdk_bedrock_agent_runtime.types.parameters
        out["parameters"] = aws_sdk_bedrock_agent_runtime.types.parameters.deserialize_json(data["parameters"])
    if "requestBody" in data:
        import aws_sdk_bedrock_agent_runtime.types.request_body
        out["request_body"] = aws_sdk_bedrock_agent_runtime.types.request_body.deserialize_json(data["requestBody"])
    if "function" in data:
        out["function"] = data["function"]
    if "executionType" in data:
        import aws_sdk_bedrock_agent_runtime.types.execution_type
        out["execution_type"] = aws_sdk_bedrock_agent_runtime.types.execution_type.deserialize_json(data["executionType"])
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    return out