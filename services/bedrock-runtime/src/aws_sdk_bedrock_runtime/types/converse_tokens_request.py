"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseTokensRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.messages
    import aws_sdk_bedrock_runtime.types.system_content_blocks
    import aws_sdk_bedrock_runtime.types.tool_configuration


class ConverseTokensRequest(TypedDict):
    messages: NotRequired["aws_sdk_bedrock_runtime.types.messages.Messages"]
    """<p>An array of messages to count tokens for.</p>"""
    system: NotRequired[
        "aws_sdk_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
    ]
    """<p>The system content blocks to count tokens for. System content provides instructions or context to the model about how it should behave or respond. The token count will include any system content provided.</p>"""
    tool_config: NotRequired[
        "aws_sdk_bedrock_runtime.types.tool_configuration.ToolConfiguration"
    ]
    """<p>The toolConfig of Converse input request to count tokens for. Configuration information for the tools that the model can use when generating a response.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>The additionalModelRequestFields of Converse input request to count tokens for. Use this field when you want to pass additional parameters that the model supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseTokensRequest) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_bedrock_runtime.types.messages

        out["messages"] = aws_sdk_bedrock_runtime.types.messages.serialize_json(
            value["messages"]
        )
    if "system" in value:
        import aws_sdk_bedrock_runtime.types.system_content_blocks

        out["system"] = (
            aws_sdk_bedrock_runtime.types.system_content_blocks.serialize_json(
                value["system"]
            )
        )
    if "tool_config" in value:
        import aws_sdk_bedrock_runtime.types.tool_configuration

        out["toolConfig"] = (
            aws_sdk_bedrock_runtime.types.tool_configuration.serialize_json(
                value["tool_config"]
            )
        )
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> ConverseTokensRequest:
    out: ConverseTokensRequest = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_bedrock_runtime.types.messages

        out["messages"] = aws_sdk_bedrock_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    if "system" in data:
        import aws_sdk_bedrock_runtime.types.system_content_blocks

        out["system"] = (
            aws_sdk_bedrock_runtime.types.system_content_blocks.deserialize_json(
                data["system"]
            )
        )
    if "toolConfig" in data:
        import aws_sdk_bedrock_runtime.types.tool_configuration

        out["tool_config"] = (
            aws_sdk_bedrock_runtime.types.tool_configuration.deserialize_json(
                data["toolConfig"]
            )
        )
    if "additionalModelRequestFields" in data:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out
