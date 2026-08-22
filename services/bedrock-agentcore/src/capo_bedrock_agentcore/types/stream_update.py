"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StreamUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.automation_stream_update


class _StreamUpdate_automationStreamUpdate(TypedDict, closed=True):
    automationStreamUpdate: (
        "capo_bedrock_agentcore.types.automation_stream_update.AutomationStreamUpdate"
    )


StreamUpdate: TypeAlias = _StreamUpdate_automationStreamUpdate


# --- restJson1 ser/de ---
def serialize_json(value: StreamUpdate) -> dict:
    if "automationStreamUpdate" in value:
        import capo_bedrock_agentcore.types.automation_stream_update

        return {
            "automationStreamUpdate": capo_bedrock_agentcore.types.automation_stream_update.serialize_json(
                value["automationStreamUpdate"]
            )
        }
    else:
        raise SerializationError("StreamUpdate: no variant present")


def deserialize_json(data: dict) -> StreamUpdate:
    if data.get("automationStreamUpdate") is not None:
        import capo_bedrock_agentcore.types.automation_stream_update

        return {
            "automationStreamUpdate": capo_bedrock_agentcore.types.automation_stream_update.deserialize_json(
                data["automationStreamUpdate"]
            )
        }
    else:
        raise DeserializationError("StreamUpdate: no recognized variant key")
