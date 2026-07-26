"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TraceElements``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_traces


class _TraceElements_agentTraces(TypedDict, closed=True):
    agentTraces: "capo_bedrock_agent_runtime.types.agent_traces.AgentTraces"


TraceElements: TypeAlias = _TraceElements_agentTraces


# --- restJson1 ser/de ---
def serialize_json(value: TraceElements) -> dict:
    if "agentTraces" in value:
        import capo_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": capo_bedrock_agent_runtime.types.agent_traces.serialize_json(
                value["agentTraces"]
            )
        }
    else:
        raise SerializationError("TraceElements: no variant present")


def deserialize_json(data: dict) -> TraceElements:
    if "agentTraces" in data:
        import capo_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": capo_bedrock_agent_runtime.types.agent_traces.deserialize_json(
                data["agentTraces"]
            )
        }
    else:
        raise DeserializationError("TraceElements: no recognized variant key")
