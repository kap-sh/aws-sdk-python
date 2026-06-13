"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseBlockStart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_name
    import aws_sdk_bedrock_runtime.types.tool_use_id
    import aws_sdk_bedrock_runtime.types.tool_use_type


class ToolUseBlockStart(TypedDict):
    tool_use_id: "aws_sdk_bedrock_runtime.types.tool_use_id.ToolUseId"
    """<p>The ID for the tool request.</p>"""
    name: "aws_sdk_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the tool that the model is requesting to use.</p>"""
    type: NotRequired["aws_sdk_bedrock_runtime.types.tool_use_type.ToolUseType"]
    """<p>The type for the tool request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseBlockStart) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_bedrock_runtime.types.tool_use_type

        out["type"] = aws_sdk_bedrock_runtime.types.tool_use_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> ToolUseBlockStart:
    out: ToolUseBlockStart = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("ToolUseBlockStart.tool_use_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ToolUseBlockStart.name required")
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.tool_use_type

        out["type"] = aws_sdk_bedrock_runtime.types.tool_use_type.deserialize_json(
            data["type"]
        )
    return out
