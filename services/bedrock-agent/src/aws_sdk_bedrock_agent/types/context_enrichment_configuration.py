"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContextEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration
    import aws_sdk_bedrock_agent.types.context_enrichment_type


class ContextEnrichmentConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.context_enrichment_type.ContextEnrichmentType"
    """<p>The method used for context enrichment. It must be Amazon Bedrock foundation models.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.BedrockFoundationModelContextEnrichmentConfiguration"
    ]
    """<p>The configuration of the Amazon Bedrock foundation model used for context enrichment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextEnrichmentConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.context_enrichment_type

    out["type"] = aws_sdk_bedrock_agent.types.context_enrichment_type.serialize_json(
        value["type"]
    )
    if "bedrock_foundation_model_configuration" in value:
        import aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration

        out["bedrockFoundationModelConfiguration"] = (
            aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContextEnrichmentConfiguration:
    out: ContextEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.context_enrichment_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.context_enrichment_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ContextEnrichmentConfiguration.type required")
    if "bedrockFoundationModelConfiguration" in data:
        import aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration

        out["bedrock_foundation_model_configuration"] = (
            aws_sdk_bedrock_agent.types.bedrock_foundation_model_context_enrichment_configuration.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    return out
