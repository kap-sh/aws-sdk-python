"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComponentConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.component_identifier
    import aws_sdk_bedrock_agentcore_control.types.component_configuration

ComponentConfigurationMap: TypeAlias = dict["aws_sdk_bedrock_agentcore_control.types.component_identifier.ComponentIdentifier", "aws_sdk_bedrock_agentcore_control.types.component_configuration.ComponentConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_agentcore_control.types.component_configuration
        out[key] = aws_sdk_bedrock_agentcore_control.types.component_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComponentConfigurationMap:
    out: ComponentConfigurationMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_agentcore_control.types.component_configuration
        out[key] = aws_sdk_bedrock_agentcore_control.types.component_configuration.deserialize_json(value)
    return out