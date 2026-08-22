"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMessages``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.messages_list


class _ExtractionJobMessages_messagesList(TypedDict, closed=True):
    messagesList: "capo_bedrock_agentcore.types.messages_list.MessagesList"


ExtractionJobMessages: TypeAlias = _ExtractionJobMessages_messagesList


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMessages) -> dict:
    if "messagesList" in value:
        import capo_bedrock_agentcore.types.messages_list

        return {
            "messagesList": capo_bedrock_agentcore.types.messages_list.serialize_json(
                value["messagesList"]
            )
        }
    else:
        raise SerializationError("ExtractionJobMessages: no variant present")


def deserialize_json(data: dict) -> ExtractionJobMessages:
    if data.get("messagesList") is not None:
        import capo_bedrock_agentcore.types.messages_list

        return {
            "messagesList": capo_bedrock_agentcore.types.messages_list.deserialize_json(
                data["messagesList"]
            )
        }
    else:
        raise DeserializationError("ExtractionJobMessages: no recognized variant key")
