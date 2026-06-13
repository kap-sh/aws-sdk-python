"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Message``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.content_blocks
    import aws_sdk_bedrock_agent_runtime.types.conversation_role


class Message(TypedDict):
    role: "aws_sdk_bedrock_agent_runtime.types.conversation_role.ConversationRole"
    """<p>The message's role.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.content_blocks.ContentBlocks"
    """<p>The message's content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.conversation_role

    out["role"] = aws_sdk_bedrock_agent_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    import aws_sdk_bedrock_agent_runtime.types.content_blocks

    out["content"] = aws_sdk_bedrock_agent_runtime.types.content_blocks.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_bedrock_agent_runtime.types.conversation_role

        out["role"] = (
            aws_sdk_bedrock_agent_runtime.types.conversation_role.deserialize_json(
                data["role"]
            )
        )
    else:
        raise DeserializationError("Message.role required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.content_blocks

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("Message.content required")
    return out
