"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_name
    import aws_sdk_bedrock_runtime.types.tool_use_id
    import aws_sdk_bedrock_runtime.types.tool_use_type


class ToolUseBlock(TypedDict, closed=True):
    tool_use_id: "aws_sdk_bedrock_runtime.types.tool_use_id.ToolUseId"
    """<p>The ID for the tool request.</p>"""
    name: "aws_sdk_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the tool that the model wants to use.</p>"""
    input: "object"
    """<p>The input to pass to the tool. </p>"""
    type: NotRequired["aws_sdk_bedrock_runtime.types.tool_use_type.ToolUseType"]
    """<p>The type for the tool request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseBlock) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    out["input"] = value["input"]
    if "type" in value:
        import aws_sdk_bedrock_runtime.types.tool_use_type

        out["type"] = aws_sdk_bedrock_runtime.types.tool_use_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> ToolUseBlock:
    out: ToolUseBlock = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("ToolUseBlock.tool_use_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ToolUseBlock.name required")
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError("ToolUseBlock.input required")
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.tool_use_type

        out["type"] = aws_sdk_bedrock_runtime.types.tool_use_type.deserialize_json(
            data["type"]
        )
    return out
