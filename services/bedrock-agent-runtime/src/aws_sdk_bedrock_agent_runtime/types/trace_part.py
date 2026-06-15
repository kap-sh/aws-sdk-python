"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TracePart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_alias_id
    import aws_sdk_bedrock_agent_runtime.types.agent_id
    import aws_sdk_bedrock_agent_runtime.types.agent_version
    import aws_sdk_bedrock_agent_runtime.types.caller_chain
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.name
    import aws_sdk_bedrock_agent_runtime.types.session_id
    import aws_sdk_bedrock_agent_runtime.types.trace


class TracePart(TypedDict):
    session_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session with the agent.</p>"""
    trace: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace.Trace"]
    r"""<p>Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement\">Trace enablement</a>.</p>"""
    caller_chain: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.caller_chain.CallerChain"
    ]
    """<p>The part's caller chain.</p>"""
    event_time: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p> The time of the trace. </p>"""
    collaborator_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.name.Name"]
    """<p>The part's collaborator name.</p>"""
    agent_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.agent_id.AgentId"]
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_id: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId"
    ]
    """<p>The unique identifier of the alias of the agent.</p>"""
    agent_version: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_version.AgentVersion"
    ]
    """<p>The version of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TracePart) -> dict:
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
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "agent_alias_id" in value:
        out["agentAliasId"] = value["agent_alias_id"]
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    return out


def deserialize_json(data: dict) -> TracePart:
    out: TracePart = {}  # type: ignore[typeddict-item]
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
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "agentAliasId" in data:
        out["agent_alias_id"] = data["agentAliasId"]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    return out
