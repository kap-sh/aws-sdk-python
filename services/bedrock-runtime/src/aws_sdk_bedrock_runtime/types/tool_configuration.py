"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_choice
    import aws_sdk_bedrock_runtime.types.tools


class ToolConfiguration(TypedDict):
    tools: "aws_sdk_bedrock_runtime.types.tools.Tools"
    """<p>An array of tools that you want to pass to a model. </p>"""
    tool_choice: NotRequired["aws_sdk_bedrock_runtime.types.tool_choice.ToolChoice"]
    """<p>If supported by model, forces the model to request a tool. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.tools

    out["tools"] = aws_sdk_bedrock_runtime.types.tools.serialize_json(value["tools"])
    if "tool_choice" in value:
        import aws_sdk_bedrock_runtime.types.tool_choice

        out["toolChoice"] = aws_sdk_bedrock_runtime.types.tool_choice.serialize_json(
            value["tool_choice"]
        )
    return out


def deserialize_json(data: dict) -> ToolConfiguration:
    out: ToolConfiguration = {}  # type: ignore[typeddict-item]
    if "tools" in data:
        import aws_sdk_bedrock_runtime.types.tools

        out["tools"] = aws_sdk_bedrock_runtime.types.tools.deserialize_json(
            data["tools"]
        )
    else:
        raise DeserializationError("ToolConfiguration.tools required")
    if "toolChoice" in data:
        import aws_sdk_bedrock_runtime.types.tool_choice

        out["tool_choice"] = aws_sdk_bedrock_runtime.types.tool_choice.deserialize_json(
            data["toolChoice"]
        )
    return out
