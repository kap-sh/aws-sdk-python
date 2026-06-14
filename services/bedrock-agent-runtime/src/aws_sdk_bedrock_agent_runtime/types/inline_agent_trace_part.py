"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentTracePart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.caller_chain
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.name
    import aws_sdk_bedrock_agent_runtime.types.session_id
    import aws_sdk_bedrock_agent_runtime.types.trace


class InlineAgentTracePart(TypedDict):
    session_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session with the agent.</p>"""
    trace: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace.Trace"]
    r"""<p>Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement\">Trace enablement</a>. </p>"""
    caller_chain: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.caller_chain.CallerChain"
    ]
    """<p>The caller chain for the trace part.</p>"""
    event_time: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time that trace occurred. </p>"""
    collaborator_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.name.Name"]
    """<p>The collaborator name for the trace part.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentTracePart) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "trace" in value:
        import aws_sdk_bedrock_agent_runtime.types.trace

        out["trace"] = aws_sdk_bedrock_agent_runtime.types.trace.serialize_json(
            value["trace"]
        )
    if "caller_chain" in value:
        import aws_sdk_bedrock_agent_runtime.types.caller_chain

        out["callerChain"] = (
            aws_sdk_bedrock_agent_runtime.types.caller_chain.serialize_json(
                value["caller_chain"]
            )
        )
    if "event_time" in value:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["eventTime"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["event_time"]
            )
        )
    if "collaborator_name" in value:
        out["collaboratorName"] = value["collaborator_name"]
    return out


def deserialize_json(data: dict) -> InlineAgentTracePart:
    out: InlineAgentTracePart = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "trace" in data:
        import aws_sdk_bedrock_agent_runtime.types.trace

        out["trace"] = aws_sdk_bedrock_agent_runtime.types.trace.deserialize_json(
            data["trace"]
        )
    if "callerChain" in data:
        import aws_sdk_bedrock_agent_runtime.types.caller_chain

        out["caller_chain"] = (
            aws_sdk_bedrock_agent_runtime.types.caller_chain.deserialize_json(
                data["callerChain"]
            )
        )
    if "eventTime" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["event_time"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["eventTime"]
            )
        )
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    return out
