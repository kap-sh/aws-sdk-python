"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#VectorSearchBedrockRerankingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking
    import aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration


class VectorSearchBedrockRerankingConfiguration(TypedDict):
    model_configuration: "aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration.VectorSearchBedrockRerankingModelConfiguration"
    """<p>Contains configurations for the reranker model.</p>"""
    number_of_reranked_results: NotRequired["int"]
    """<p>The number of results to return after reranking.</p>"""
    metadata_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking.MetadataConfigurationForReranking"
    ]
    """<p>Contains configurations for the metadata to use in reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchBedrockRerankingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration

    out["modelConfiguration"] = (
        aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    if "number_of_reranked_results" in value:
        out["numberOfRerankedResults"] = value["number_of_reranked_results"]
    if "metadata_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking

        out["metadataConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking.serialize_json(
                value["metadata_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchBedrockRerankingConfiguration:
    out: VectorSearchBedrockRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if "modelConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration

        out["model_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.vector_search_bedrock_reranking_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "VectorSearchBedrockRerankingConfiguration.model_configuration required"
        )
    if "numberOfRerankedResults" in data:
        out["number_of_reranked_results"] = data["numberOfRerankedResults"]
    if "metadataConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking

        out["metadata_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.metadata_configuration_for_reranking.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    return out
