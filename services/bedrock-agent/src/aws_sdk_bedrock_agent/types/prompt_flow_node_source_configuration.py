"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration
    import aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration


class _PromptFlowNodeSourceConfiguration_resource(TypedDict):
    resource: "aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration.PromptFlowNodeResourceConfiguration"


class _PromptFlowNodeSourceConfiguration_inline(TypedDict):
    inline: "aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration.PromptFlowNodeInlineConfiguration"


PromptFlowNodeSourceConfiguration: TypeAlias = (
    _PromptFlowNodeSourceConfiguration_resource
    | _PromptFlowNodeSourceConfiguration_inline
)


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeSourceConfiguration) -> dict:
    if "resource" in value:
        import aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration

        return {
            "resource": aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration.serialize_json(
                value["resource"]
            )
        }
    elif "inline" in value:
        import aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration

        return {
            "inline": aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration.serialize_json(
                value["inline"]
            )
        }
    else:
        raise SerializationError(
            "PromptFlowNodeSourceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> PromptFlowNodeSourceConfiguration:
    if "resource" in data:
        import aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration

        return {
            "resource": aws_sdk_bedrock_agent.types.prompt_flow_node_resource_configuration.deserialize_json(
                data["resource"]
            )
        }
    elif "inline" in data:
        import aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration

        return {
            "inline": aws_sdk_bedrock_agent.types.prompt_flow_node_inline_configuration.deserialize_json(
                data["inline"]
            )
        }
    else:
        raise DeserializationError(
            "PromptFlowNodeSourceConfiguration: no recognized variant key"
        )
