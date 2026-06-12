"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ToolChoice``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.any_tool_choice
    import aws_sdk_bedrock_agent.types.auto_tool_choice
    import aws_sdk_bedrock_agent.types.specific_tool_choice


class _ToolChoice_auto(TypedDict):
    auto: "aws_sdk_bedrock_agent.types.auto_tool_choice.AutoToolChoice"


class _ToolChoice_any(TypedDict):
    any: "aws_sdk_bedrock_agent.types.any_tool_choice.AnyToolChoice"


class _ToolChoice_tool(TypedDict):
    tool: "aws_sdk_bedrock_agent.types.specific_tool_choice.SpecificToolChoice"


ToolChoice: TypeAlias = _ToolChoice_auto | _ToolChoice_any | _ToolChoice_tool


# --- restJson1 ser/de ---
def serialize_json(value: ToolChoice) -> dict:
    if "auto" in value:
        import aws_sdk_bedrock_agent.types.auto_tool_choice

        return {
            "auto": aws_sdk_bedrock_agent.types.auto_tool_choice.serialize_json(
                value["auto"]
            )
        }
    elif "any" in value:
        import aws_sdk_bedrock_agent.types.any_tool_choice

        return {
            "any": aws_sdk_bedrock_agent.types.any_tool_choice.serialize_json(
                value["any"]
            )
        }
    elif "tool" in value:
        import aws_sdk_bedrock_agent.types.specific_tool_choice

        return {
            "tool": aws_sdk_bedrock_agent.types.specific_tool_choice.serialize_json(
                value["tool"]
            )
        }
    else:
        raise SerializationError("ToolChoice: no variant present")


def deserialize_json(data: dict) -> ToolChoice:
    if "auto" in data:
        import aws_sdk_bedrock_agent.types.auto_tool_choice

        return {
            "auto": aws_sdk_bedrock_agent.types.auto_tool_choice.deserialize_json(
                data["auto"]
            )
        }
    elif "any" in data:
        import aws_sdk_bedrock_agent.types.any_tool_choice

        return {
            "any": aws_sdk_bedrock_agent.types.any_tool_choice.deserialize_json(
                data["any"]
            )
        }
    elif "tool" in data:
        import aws_sdk_bedrock_agent.types.specific_tool_choice

        return {
            "tool": aws_sdk_bedrock_agent.types.specific_tool_choice.deserialize_json(
                data["tool"]
            )
        }
    else:
        raise DeserializationError("ToolChoice: no recognized variant key")
