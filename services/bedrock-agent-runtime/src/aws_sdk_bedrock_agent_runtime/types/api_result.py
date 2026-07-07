"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.api_path
    import aws_sdk_bedrock_agent_runtime.types.confirmation_state
    import aws_sdk_bedrock_agent_runtime.types.response_body
    import aws_sdk_bedrock_agent_runtime.types.response_state


class ApiResult(TypedDict, closed=True):
    action_group: "str"
    """<p>The action group that the API operation belongs to.</p>"""
    http_method: NotRequired["str"]
    """<p>The HTTP method for the API operation.</p>"""
    api_path: NotRequired["aws_sdk_bedrock_agent_runtime.types.api_path.ApiPath"]
    """<p>The path to the API operation.</p>"""
    confirmation_state: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.confirmation_state.ConfirmationState"
    ]
    """<p>Controls the API operations or functions to invoke based on the user confirmation.</p>"""
    response_state: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.response_state.ResponseState"
    ]
    """<p>Controls the final response state returned to end user when API/Function execution failed. When this state is FAILURE, the request would fail with dependency failure exception. When this state is REPROMPT, the API/function response will be sent to model for re-prompt</p>"""
    http_status_code: NotRequired["int"]
    """<p>http status code from API execution response (for example: 200, 400, 500).</p>"""
    response_body: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.response_body.ResponseBody"
    ]
    """<p>The response body from the API operation. The key of the object is the content type (currently, only <code>TEXT</code> is supported). The response may be returned directly or from the Lambda function.</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiResult) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "http_method" in value:
        out["httpMethod"] = value["http_method"]
    if "api_path" in value:
        out["apiPath"] = value["api_path"]
    if "confirmation_state" in value:
        import aws_sdk_bedrock_agent_runtime.types.confirmation_state

        out["confirmationState"] = (
            aws_sdk_bedrock_agent_runtime.types.confirmation_state.serialize_json(
                value["confirmation_state"]
            )
        )
    if "response_state" in value:
        import aws_sdk_bedrock_agent_runtime.types.response_state

        out["responseState"] = (
            aws_sdk_bedrock_agent_runtime.types.response_state.serialize_json(
                value["response_state"]
            )
        )
    if "http_status_code" in value:
        out["httpStatusCode"] = value["http_status_code"]
    if "response_body" in value:
        import aws_sdk_bedrock_agent_runtime.types.response_body

        out["responseBody"] = (
            aws_sdk_bedrock_agent_runtime.types.response_body.serialize_json(
                value["response_body"]
            )
        )
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    return out


def deserialize_json(data: dict) -> ApiResult:
    out: ApiResult = {}  # type: ignore[typeddict-item]
    if "actionGroup" in data:
        out["action_group"] = data["actionGroup"]
    else:
        raise DeserializationError("ApiResult.action_group required")
    if "httpMethod" in data:
        out["http_method"] = data["httpMethod"]
    if "apiPath" in data:
        out["api_path"] = data["apiPath"]
    if "confirmationState" in data:
        import aws_sdk_bedrock_agent_runtime.types.confirmation_state

        out["confirmation_state"] = (
            aws_sdk_bedrock_agent_runtime.types.confirmation_state.deserialize_json(
                data["confirmationState"]
            )
        )
    if "responseState" in data:
        import aws_sdk_bedrock_agent_runtime.types.response_state

        out["response_state"] = (
            aws_sdk_bedrock_agent_runtime.types.response_state.deserialize_json(
                data["responseState"]
            )
        )
    if "httpStatusCode" in data:
        out["http_status_code"] = data["httpStatusCode"]
    if "responseBody" in data:
        import aws_sdk_bedrock_agent_runtime.types.response_body

        out["response_body"] = (
            aws_sdk_bedrock_agent_runtime.types.response_body.deserialize_json(
                data["responseBody"]
            )
        )
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    return out
