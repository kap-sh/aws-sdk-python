"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Memory``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.memory_session_summary


class _Memory_sessionSummary(TypedDict, closed=True):
    sessionSummary: (
        "capo_bedrock_agent_runtime.types.memory_session_summary.MemorySessionSummary"
    )


Memory: TypeAlias = _Memory_sessionSummary


# --- restJson1 ser/de ---
def serialize_json(value: Memory) -> dict:
    if "sessionSummary" in value:
        import capo_bedrock_agent_runtime.types.memory_session_summary

        return {
            "sessionSummary": capo_bedrock_agent_runtime.types.memory_session_summary.serialize_json(
                value["sessionSummary"]
            )
        }
    else:
        raise SerializationError("Memory: no variant present")


def deserialize_json(data: dict) -> Memory:
    if "sessionSummary" in data:
        import capo_bedrock_agent_runtime.types.memory_session_summary

        return {
            "sessionSummary": capo_bedrock_agent_runtime.types.memory_session_summary.deserialize_json(
                data["sessionSummary"]
            )
        }
    else:
        raise DeserializationError("Memory: no recognized variant key")
