"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VectorSearchRerankingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration
    import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type


class VectorSearchRerankingConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type.VectorSearchRerankingConfigurationType"
    """<p>Specifies the type of reranking model to use. Currently, the only supported value is <code>BEDROCK_RERANKING_MODEL</code>.</p>"""
    bedrock_reranking_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration.VectorSearchBedrockRerankingConfiguration"
    ]
    """<p>Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchRerankingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type

    out["type"] = (
        aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_reranking_configuration" in value:
        import aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration

        out["bedrockRerankingConfiguration"] = (
            aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration.serialize_json(
                value["bedrock_reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchRerankingConfiguration:
    out: VectorSearchRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.vector_search_reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("VectorSearchRerankingConfiguration.type required")
    if "bedrockRerankingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            aws_sdk_bedrock_agent.types.vector_search_bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    return out
