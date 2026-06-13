"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#MessageStartEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.conversation_role


class MessageStartEvent(TypedDict):
    role: "aws_sdk_bedrock_runtime.types.conversation_role.ConversationRole"
    """<p>The role for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageStartEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.conversation_role

    out["role"] = aws_sdk_bedrock_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    return out


def deserialize_json(data: dict) -> MessageStartEvent:
    out: MessageStartEvent = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_bedrock_runtime.types.conversation_role

        out["role"] = aws_sdk_bedrock_runtime.types.conversation_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("MessageStartEvent.role required")
    return out
