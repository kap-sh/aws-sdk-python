"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Message``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.content_blocks
    import aws_sdk_bedrock_runtime.types.conversation_role


class Message(TypedDict):
    role: "aws_sdk_bedrock_runtime.types.conversation_role.ConversationRole"
    """<p>The role that the message plays in the message.</p>"""
    content: "aws_sdk_bedrock_runtime.types.content_blocks.ContentBlocks"
    """<p>The message content. Note the following restrictions:</p> <ul> <li> <p>You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.</p> </li> <li> <p>You can include up to five documents. Each document's size must be no more than 4.5 MB.</p> </li> <li> <p>If you include a <code>ContentBlock</code> with a <code>document</code> field in the array, you must also include a <code>ContentBlock</code> with a <code>text</code> field.</p> </li> <li> <p>You can only include images and documents if the <code>role</code> is <code>user</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.conversation_role

    out["role"] = aws_sdk_bedrock_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    import aws_sdk_bedrock_runtime.types.content_blocks

    out["content"] = aws_sdk_bedrock_runtime.types.content_blocks.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_bedrock_runtime.types.conversation_role

        out["role"] = aws_sdk_bedrock_runtime.types.conversation_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("Message.role required")
    if "content" in data:
        import aws_sdk_bedrock_runtime.types.content_blocks

        out["content"] = aws_sdk_bedrock_runtime.types.content_blocks.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("Message.content required")
    return out
