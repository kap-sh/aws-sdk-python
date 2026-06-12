"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnectionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration
    import aws_sdk_bedrock_agent.types.flow_data_connection_configuration


class _FlowConnectionConfiguration_data(TypedDict):
    data: "aws_sdk_bedrock_agent.types.flow_data_connection_configuration.FlowDataConnectionConfiguration"


class _FlowConnectionConfiguration_conditional(TypedDict):
    conditional: "aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration.FlowConditionalConnectionConfiguration"


FlowConnectionConfiguration: TypeAlias = (
    _FlowConnectionConfiguration_data | _FlowConnectionConfiguration_conditional
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnectionConfiguration) -> dict:
    if "data" in value:
        import aws_sdk_bedrock_agent.types.flow_data_connection_configuration

        return {
            "data": aws_sdk_bedrock_agent.types.flow_data_connection_configuration.serialize_json(
                value["data"]
            )
        }
    elif "conditional" in value:
        import aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration

        return {
            "conditional": aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration.serialize_json(
                value["conditional"]
            )
        }
    else:
        raise SerializationError("FlowConnectionConfiguration: no variant present")


def deserialize_json(data: dict) -> FlowConnectionConfiguration:
    if "data" in data:
        import aws_sdk_bedrock_agent.types.flow_data_connection_configuration

        return {
            "data": aws_sdk_bedrock_agent.types.flow_data_connection_configuration.deserialize_json(
                data["data"]
            )
        }
    elif "conditional" in data:
        import aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration

        return {
            "conditional": aws_sdk_bedrock_agent.types.flow_conditional_connection_configuration.deserialize_json(
                data["conditional"]
            )
        }
    else:
        raise DeserializationError(
            "FlowConnectionConfiguration: no recognized variant key"
        )
