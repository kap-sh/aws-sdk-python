"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle
    import aws_sdk_bedrock_agentcore.types.tool_description_text_input


class _ToolDescriptionSource_toolDescriptionText(TypedDict, closed=True):
    toolDescriptionText: "aws_sdk_bedrock_agentcore.types.tool_description_text_input.ToolDescriptionTextInput"


class _ToolDescriptionSource_configurationBundle(TypedDict, closed=True):
    configurationBundle: "aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle.ToolDescriptionConfigurationBundle"


ToolDescriptionSource: TypeAlias = (
    _ToolDescriptionSource_toolDescriptionText
    | _ToolDescriptionSource_configurationBundle
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionSource) -> dict:
    if "toolDescriptionText" in value:
        import aws_sdk_bedrock_agentcore.types.tool_description_text_input

        return {
            "toolDescriptionText": aws_sdk_bedrock_agentcore.types.tool_description_text_input.serialize_json(
                value["toolDescriptionText"]
            )
        }
    elif "configurationBundle" in value:
        import aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle

        return {
            "configurationBundle": aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle.serialize_json(
                value["configurationBundle"]
            )
        }
    else:
        raise SerializationError("ToolDescriptionSource: no variant present")


def deserialize_json(data: dict) -> ToolDescriptionSource:
    if "toolDescriptionText" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_text_input

        return {
            "toolDescriptionText": aws_sdk_bedrock_agentcore.types.tool_description_text_input.deserialize_json(
                data["toolDescriptionText"]
            )
        }
    elif "configurationBundle" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle

        return {
            "configurationBundle": aws_sdk_bedrock_agentcore.types.tool_description_configuration_bundle.deserialize_json(
                data["configurationBundle"]
            )
        }
    else:
        raise DeserializationError("ToolDescriptionSource: no recognized variant key")
