"""Generated from Smithy shape ``com.amazonaws.qbusiness#CopyFromSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.conversation_source


class _CopyFromSource_conversation(TypedDict, closed=True):
    conversation: "capo_qbusiness.types.conversation_source.ConversationSource"


CopyFromSource: TypeAlias = _CopyFromSource_conversation


# --- restJson1 ser/de ---
def serialize_json(value: CopyFromSource) -> dict:
    if "conversation" in value:
        import capo_qbusiness.types.conversation_source

        return {
            "conversation": capo_qbusiness.types.conversation_source.serialize_json(
                value["conversation"]
            )
        }
    else:
        raise SerializationError("CopyFromSource: no variant present")


def deserialize_json(data: dict) -> CopyFromSource:
    if "conversation" in data:
        import capo_qbusiness.types.conversation_source

        return {
            "conversation": capo_qbusiness.types.conversation_source.deserialize_json(
                data["conversation"]
            )
        }
    else:
        raise DeserializationError("CopyFromSource: no recognized variant key")
