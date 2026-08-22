"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnectionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_conditional_connection_configuration
    import capo_bedrock_agent.types.flow_data_connection_configuration


class _FlowConnectionConfiguration_data(TypedDict, closed=True):
    data: "capo_bedrock_agent.types.flow_data_connection_configuration.FlowDataConnectionConfiguration"


class _FlowConnectionConfiguration_conditional(TypedDict, closed=True):
    conditional: "capo_bedrock_agent.types.flow_conditional_connection_configuration.FlowConditionalConnectionConfiguration"


FlowConnectionConfiguration: TypeAlias = (
    _FlowConnectionConfiguration_data | _FlowConnectionConfiguration_conditional
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnectionConfiguration) -> dict:
    if "data" in value:
        import capo_bedrock_agent.types.flow_data_connection_configuration

        return {
            "data": capo_bedrock_agent.types.flow_data_connection_configuration.serialize_json(
                value["data"]
            )
        }
    elif "conditional" in value:
        import capo_bedrock_agent.types.flow_conditional_connection_configuration

        return {
            "conditional": capo_bedrock_agent.types.flow_conditional_connection_configuration.serialize_json(
                value["conditional"]
            )
        }
    else:
        raise SerializationError("FlowConnectionConfiguration: no variant present")


def deserialize_json(data: dict) -> FlowConnectionConfiguration:
    if data.get("data") is not None:
        import capo_bedrock_agent.types.flow_data_connection_configuration

        return {
            "data": capo_bedrock_agent.types.flow_data_connection_configuration.deserialize_json(
                data["data"]
            )
        }
    elif data.get("conditional") is not None:
        import capo_bedrock_agent.types.flow_conditional_connection_configuration

        return {
            "conditional": capo_bedrock_agent.types.flow_conditional_connection_configuration.deserialize_json(
                data["conditional"]
            )
        }
    else:
        raise DeserializationError(
            "FlowConnectionConfiguration: no recognized variant key"
        )
