"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration_data
    import aws_sdk_qconnect.types.ai_agent_type

AIAgentConfigurationMap: TypeAlias = dict[
    "aws_sdk_qconnect.types.ai_agent_type.AIAgentType",
    "aws_sdk_qconnect.types.ai_agent_configuration_data.AIAgentConfigurationData",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AIAgentConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_qconnect.types.ai_agent_configuration_data

        out[key] = aws_sdk_qconnect.types.ai_agent_configuration_data.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> AIAgentConfigurationMap:
    out: AIAgentConfigurationMap = {}
    for key, value in data.items():
        import aws_sdk_qconnect.types.ai_agent_configuration_data

        out[key] = aws_sdk_qconnect.types.ai_agent_configuration_data.deserialize_json(
            value
        )
    return out
