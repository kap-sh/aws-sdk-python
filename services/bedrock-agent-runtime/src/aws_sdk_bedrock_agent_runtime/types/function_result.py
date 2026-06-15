"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FunctionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.confirmation_state
    import aws_sdk_bedrock_agent_runtime.types.response_body
    import aws_sdk_bedrock_agent_runtime.types.response_state


class FunctionResult(TypedDict):
    action_group: "str"
    """<p>The action group that the function belongs to.</p>"""
    confirmation_state: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.confirmation_state.ConfirmationState"
    ]
    """<p>Contains the user confirmation information about the function that was called.</p>"""
    function: NotRequired["str"]
    """<p>The name of the function that was called.</p>"""
    response_body: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.response_body.ResponseBody"
    ]
    r"""<p>The response from the function call using the parameters. The response might be returned directly or from the Lambda function. Specify <code>TEXT</code> or <code>IMAGES</code>. The key of the object is the content type. You can only specify one type. If you specify <code>IMAGES</code>, you can specify only one image. You can specify images only when the function in the <code>returnControlInvocationResults</code> is a computer use action. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html\">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>.</p>"""
    response_state: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.response_state.ResponseState"
    ]
    """<p>Controls the final response state returned to end user when API/Function execution failed. When this state is FAILURE, the request would fail with dependency failure exception. When this state is REPROMPT, the API/function response will be sent to model for re-prompt</p>"""
    agent_id: NotRequired["str"]
    """<p>The agent's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionResult) -> dict:
    out: dict = {}
    out["actionGroup"] = value["action_group"]
    if "confirmation_state" in value:
        import aws_sdk_bedrock_agent_runtime.types.confirmation_state

        out["confirmationState"] = (
            aws_sdk_bedrock_agent_runtime.types.confirmation_state.serialize_json(
                value["confirmation_state"]
            )
        )
    if "function" in value:
        out["function"] = value["function"]
    if "response_body" in value:
        import aws_sdk_bedrock_agent_runtime.types.response_body

        out["responseBody"] = (
            aws_sdk_bedrock_agent_runtime.types.response_body.serialize_json(
                value["response_body"]
            )
        )
    if "response_state" in value:
        import aws_sdk_bedrock_agent_runtime.types.response_state

        out["responseState"] = (
            aws_sdk_bedrock_agent_runtime.types.response_state.serialize_json(
                value["response_state"]
            )
        )
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    return out


def deserialize_json(data: dict) -> FunctionResult:
    out: FunctionResult = {}  # type: ignore[typeddict-item]
    if "actionGroup" in data:
        out["action_group"] = data["actionGroup"]
    else:
        raise DeserializationError("FunctionResult.action_group required")
    if "confirmationState" in data:
        import aws_sdk_bedrock_agent_runtime.types.confirmation_state

        out["confirmation_state"] = (
            aws_sdk_bedrock_agent_runtime.types.confirmation_state.deserialize_json(
                data["confirmationState"]
            )
        )
    if "function" in data:
        out["function"] = data["function"]
    if "responseBody" in data:
        import aws_sdk_bedrock_agent_runtime.types.response_body

        out["response_body"] = (
            aws_sdk_bedrock_agent_runtime.types.response_body.deserialize_json(
                data["responseBody"]
            )
        )
    if "responseState" in data:
        import aws_sdk_bedrock_agent_runtime.types.response_state

        out["response_state"] = (
            aws_sdk_bedrock_agent_runtime.types.response_state.deserialize_json(
                data["responseState"]
            )
        )
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    return out
