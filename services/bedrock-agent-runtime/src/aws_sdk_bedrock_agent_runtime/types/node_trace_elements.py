"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeTraceElements``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_traces


class _NodeTraceElements_agentTraces(TypedDict, closed=True):
    agentTraces: "aws_sdk_bedrock_agent_runtime.types.agent_traces.AgentTraces"


NodeTraceElements: TypeAlias = _NodeTraceElements_agentTraces


# --- restJson1 ser/de ---
def serialize_json(value: NodeTraceElements) -> dict:
    if "agentTraces" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": aws_sdk_bedrock_agent_runtime.types.agent_traces.serialize_json(
                value["agentTraces"]
            )
        }
    else:
        raise SerializationError("NodeTraceElements: no variant present")


def deserialize_json(data: dict) -> NodeTraceElements:
    if "agentTraces" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": aws_sdk_bedrock_agent_runtime.types.agent_traces.deserialize_json(
                data["agentTraces"]
            )
        }
    else:
        raise DeserializationError("NodeTraceElements: no recognized variant key")
