"""Generated from Smithy shape ``com.amazonaws.bedrock#VectorSearchRerankingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration
    import aws_sdk_bedrock.types.vector_search_reranking_configuration_type


class VectorSearchRerankingConfiguration(TypedDict):
    type: "aws_sdk_bedrock.types.vector_search_reranking_configuration_type.VectorSearchRerankingConfigurationType"
    """<p>The type of reranking to apply to vector search results. Currently, the only supported value is BEDROCK, which uses Amazon Bedrock foundation models for reranking.</p>"""
    bedrock_reranking_configuration: NotRequired[
        "aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration.VectorSearchBedrockRerankingConfiguration"
    ]
    """<p>Configuration for using Amazon Bedrock foundation models to rerank search results. This is required when the reranking type is set to BEDROCK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchRerankingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.vector_search_reranking_configuration_type

    out["type"] = (
        aws_sdk_bedrock.types.vector_search_reranking_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "bedrock_reranking_configuration" in value:
        import aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration

        out["bedrockRerankingConfiguration"] = (
            aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration.serialize_json(
                value["bedrock_reranking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchRerankingConfiguration:
    out: VectorSearchRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.vector_search_reranking_configuration_type

        out["type"] = (
            aws_sdk_bedrock.types.vector_search_reranking_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("VectorSearchRerankingConfiguration.type required")
    if "bedrockRerankingConfiguration" in data:
        import aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration

        out["bedrock_reranking_configuration"] = (
            aws_sdk_bedrock.types.vector_search_bedrock_reranking_configuration.deserialize_json(
                data["bedrockRerankingConfiguration"]
            )
        )
    return out
