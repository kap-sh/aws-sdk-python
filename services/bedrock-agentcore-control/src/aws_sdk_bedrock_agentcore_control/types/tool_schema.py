"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolSchema``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.s3_configuration
    import aws_sdk_bedrock_agentcore_control.types.tool_definitions


class _ToolSchema_s3(TypedDict):
    s3: "aws_sdk_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class _ToolSchema_inlinePayload(TypedDict):
    inlinePayload: (
        "aws_sdk_bedrock_agentcore_control.types.tool_definitions.ToolDefinitions"
    )


ToolSchema: TypeAlias = _ToolSchema_s3 | _ToolSchema_inlinePayload


# --- restJson1 ser/de ---
def serialize_json(value: ToolSchema) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": aws_sdk_bedrock_agentcore_control.types.s3_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "inlinePayload" in value:
        import aws_sdk_bedrock_agentcore_control.types.tool_definitions

        return {
            "inlinePayload": aws_sdk_bedrock_agentcore_control.types.tool_definitions.serialize_json(
                value["inlinePayload"]
            )
        }
    else:
        raise SerializationError("ToolSchema: no variant present")


def deserialize_json(data: dict) -> ToolSchema:
    if "s3" in data:
        import aws_sdk_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": aws_sdk_bedrock_agentcore_control.types.s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif "inlinePayload" in data:
        import aws_sdk_bedrock_agentcore_control.types.tool_definitions

        return {
            "inlinePayload": aws_sdk_bedrock_agentcore_control.types.tool_definitions.deserialize_json(
                data["inlinePayload"]
            )
        }
    else:
        raise DeserializationError("ToolSchema: no recognized variant key")
