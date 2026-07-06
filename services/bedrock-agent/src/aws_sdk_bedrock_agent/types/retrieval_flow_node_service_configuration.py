"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalFlowNodeServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration


class _RetrievalFlowNodeServiceConfiguration_s3(TypedDict, closed=True):
    s3: "aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration.RetrievalFlowNodeS3Configuration"


RetrievalFlowNodeServiceConfiguration: TypeAlias = (
    _RetrievalFlowNodeServiceConfiguration_s3
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFlowNodeServiceConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration

        return {
            "s3": aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "RetrievalFlowNodeServiceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RetrievalFlowNodeServiceConfiguration:
    if "s3" in data:
        import aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration

        return {
            "s3": aws_sdk_bedrock_agent.types.retrieval_flow_node_s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "RetrievalFlowNodeServiceConfiguration: no recognized variant key"
        )
