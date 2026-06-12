"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockFoundationModelContextEnrichmentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.bedrock_model_arn
    import aws_sdk_bedrock_agent.types.enrichment_strategy_configuration


class BedrockFoundationModelContextEnrichmentConfiguration(TypedDict):
    enrichment_strategy_configuration: "aws_sdk_bedrock_agent.types.enrichment_strategy_configuration.EnrichmentStrategyConfiguration"
    """<p>The enrichment stategy used to provide additional context. For example, Neptune GraphRAG uses Amazon Bedrock foundation models to perform chunk entity extraction.</p>"""
    model_arn: "aws_sdk_bedrock_agent.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelContextEnrichmentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.enrichment_strategy_configuration

    out["enrichmentStrategyConfiguration"] = (
        aws_sdk_bedrock_agent.types.enrichment_strategy_configuration.serialize_json(
            value["enrichment_strategy_configuration"]
        )
    )
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(
    data: dict,
) -> BedrockFoundationModelContextEnrichmentConfiguration:
    out: BedrockFoundationModelContextEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "enrichmentStrategyConfiguration" in data:
        import aws_sdk_bedrock_agent.types.enrichment_strategy_configuration

        out["enrichment_strategy_configuration"] = (
            aws_sdk_bedrock_agent.types.enrichment_strategy_configuration.deserialize_json(
                data["enrichmentStrategyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "BedrockFoundationModelContextEnrichmentConfiguration.enrichment_strategy_configuration required"
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "BedrockFoundationModelContextEnrichmentConfiguration.model_arn required"
        )
    return out
