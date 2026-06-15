"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineSessionState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.conversation_history
    import aws_sdk_bedrock_agent_runtime.types.input_files
    import aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map
    import aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results
    import aws_sdk_bedrock_agent_runtime.types.session_attributes_map


class InlineSessionState(TypedDict):
    session_attributes: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.session_attributes_map.SessionAttributesMap"
    ]
    """<p> Contains attributes that persist across a session and the values of those attributes. </p>"""
    prompt_session_attributes: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map.PromptSessionAttributesMap"
    ]
    """<p> Contains attributes that persist across a session and the values of those attributes. </p>"""
    return_control_invocation_results: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results.ReturnControlInvocationResults"
    ]
    r"""<p> Contains information about the results from the action group invocation. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html\">Return control to the agent developer</a>. </p> <note> <p>If you include this field in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    invocation_id: NotRequired["str"]
    r"""<p> The identifier of the invocation of an action. This value must match the <code>invocationId</code> returned in the <code>InvokeInlineAgent</code> response for the action whose results are provided in the <code>returnControlInvocationResults</code> field. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html\">Return control to the agent developer</a>. </p>"""
    files: NotRequired["aws_sdk_bedrock_agent_runtime.types.input_files.InputFiles"]
    """<p> Contains information about the files used by code interpreter. </p>"""
    conversation_history: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.conversation_history.ConversationHistory"
    ]
    """<p> Contains the conversation history that persist across sessions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineSessionState) -> dict:
    out: dict = {}
    if "session_attributes" in value:
        import aws_sdk_bedrock_agent_runtime.types.session_attributes_map

        out["sessionAttributes"] = (
            aws_sdk_bedrock_agent_runtime.types.session_attributes_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "prompt_session_attributes" in value:
        import aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map

        out["promptSessionAttributes"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map.serialize_json(
                value["prompt_session_attributes"]
            )
        )
    if "return_control_invocation_results" in value:
        import aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results

        out["returnControlInvocationResults"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results.serialize_json(
                value["return_control_invocation_results"]
            )
        )
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    if "files" in value:
        import aws_sdk_bedrock_agent_runtime.types.input_files

        out["files"] = aws_sdk_bedrock_agent_runtime.types.input_files.serialize_json(
            value["files"]
        )
    if "conversation_history" in value:
        import aws_sdk_bedrock_agent_runtime.types.conversation_history

        out["conversationHistory"] = (
            aws_sdk_bedrock_agent_runtime.types.conversation_history.serialize_json(
                value["conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineSessionState:
    out: InlineSessionState = {}  # type: ignore[typeddict-item]
    if "sessionAttributes" in data:
        import aws_sdk_bedrock_agent_runtime.types.session_attributes_map

        out["session_attributes"] = (
            aws_sdk_bedrock_agent_runtime.types.session_attributes_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if "promptSessionAttributes" in data:
        import aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map

        out["prompt_session_attributes"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_session_attributes_map.deserialize_json(
                data["promptSessionAttributes"]
            )
        )
    if "returnControlInvocationResults" in data:
        import aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results

        out["return_control_invocation_results"] = (
            aws_sdk_bedrock_agent_runtime.types.return_control_invocation_results.deserialize_json(
                data["returnControlInvocationResults"]
            )
        )
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    if "files" in data:
        import aws_sdk_bedrock_agent_runtime.types.input_files

        out["files"] = aws_sdk_bedrock_agent_runtime.types.input_files.deserialize_json(
            data["files"]
        )
    if "conversationHistory" in data:
        import aws_sdk_bedrock_agent_runtime.types.conversation_history

        out["conversation_history"] = (
            aws_sdk_bedrock_agent_runtime.types.conversation_history.deserialize_json(
                data["conversationHistory"]
            )
        )
    return out
