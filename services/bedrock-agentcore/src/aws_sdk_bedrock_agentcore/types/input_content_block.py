"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InputContentBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.body
    import aws_sdk_bedrock_agentcore.types.max_len_string


class InputContentBlock(TypedDict, closed=True):
    path: "aws_sdk_bedrock_agentcore.types.max_len_string.MaxLenString"
    """<p>The path to the input content.</p>"""
    text: NotRequired["aws_sdk_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The text input content.</p>"""
    blob: NotRequired["aws_sdk_bedrock_agentcore.types.body.Body"]
    """<p>The binary input content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputContentBlock) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "text" in value:
        out["text"] = value["text"]
    if "blob" in value:
        import aws_sdk_bedrock_agentcore.types.body

        out["blob"] = aws_sdk_bedrock_agentcore.types.body.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> InputContentBlock:
    out: InputContentBlock = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("InputContentBlock.path required")
    if "text" in data:
        out["text"] = data["text"]
    if "blob" in data:
        import aws_sdk_bedrock_agentcore.types.body

        out["blob"] = aws_sdk_bedrock_agentcore.types.body.deserialize_json(
            data["blob"]
        )
    return out
