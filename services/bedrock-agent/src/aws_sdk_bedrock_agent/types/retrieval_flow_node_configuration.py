"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration


class RetrievalFlowNodeConfiguration(TypedDict):
    service_configuration: "aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration.RetrievalFlowNodeServiceConfiguration"
    """<p>Contains configurations for the service to use for retrieving data to return as the output from the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFlowNodeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration

    out["serviceConfiguration"] = (
        aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration.serialize_json(
            value["service_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetrievalFlowNodeConfiguration:
    out: RetrievalFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "serviceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration

        out["service_configuration"] = (
            aws_sdk_bedrock_agent.types.retrieval_flow_node_service_configuration.deserialize_json(
                data["serviceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RetrievalFlowNodeConfiguration.service_configuration required"
        )
    return out
