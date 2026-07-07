"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageFlowNodeServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration


class _StorageFlowNodeServiceConfiguration_s3(TypedDict, closed=True):
    s3: "aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration.StorageFlowNodeS3Configuration"


StorageFlowNodeServiceConfiguration: TypeAlias = _StorageFlowNodeServiceConfiguration_s3


# --- restJson1 ser/de ---
def serialize_json(value: StorageFlowNodeServiceConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration

        return {
            "s3": aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "StorageFlowNodeServiceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> StorageFlowNodeServiceConfiguration:
    if "s3" in data:
        import aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration

        return {
            "s3": aws_sdk_bedrock_agent.types.storage_flow_node_s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "StorageFlowNodeServiceConfiguration: no recognized variant key"
        )
