"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VectorIngestionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.chunking_configuration
    import capo_bedrock_agent.types.context_enrichment_configuration
    import capo_bedrock_agent.types.custom_transformation_configuration
    import capo_bedrock_agent.types.parsing_configuration


class VectorIngestionConfiguration(TypedDict, closed=True):
    chunking_configuration: NotRequired[
        "capo_bedrock_agent.types.chunking_configuration.ChunkingConfiguration"
    ]
    """<p>Details about how to chunk the documents in the data source. A <i>chunk</i> refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.</p>"""
    custom_transformation_configuration: NotRequired[
        "capo_bedrock_agent.types.custom_transformation_configuration.CustomTransformationConfiguration"
    ]
    """<p>A custom document transformer for parsed data source documents.</p>"""
    parsing_configuration: NotRequired[
        "capo_bedrock_agent.types.parsing_configuration.ParsingConfiguration"
    ]
    """<p>Configurations for a parser to use for parsing documents in your data source. If you exclude this field, the default parser will be used.</p>"""
    context_enrichment_configuration: NotRequired[
        "capo_bedrock_agent.types.context_enrichment_configuration.ContextEnrichmentConfiguration"
    ]
    """<p>The context enrichment configuration used for ingestion of the data into the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorIngestionConfiguration) -> dict:
    out: dict = {}
    if "chunking_configuration" in value:
        import capo_bedrock_agent.types.chunking_configuration

        out["chunkingConfiguration"] = (
            capo_bedrock_agent.types.chunking_configuration.serialize_json(
                value["chunking_configuration"]
            )
        )
    if "custom_transformation_configuration" in value:
        import capo_bedrock_agent.types.custom_transformation_configuration

        out["customTransformationConfiguration"] = (
            capo_bedrock_agent.types.custom_transformation_configuration.serialize_json(
                value["custom_transformation_configuration"]
            )
        )
    if "parsing_configuration" in value:
        import capo_bedrock_agent.types.parsing_configuration

        out["parsingConfiguration"] = (
            capo_bedrock_agent.types.parsing_configuration.serialize_json(
                value["parsing_configuration"]
            )
        )
    if "context_enrichment_configuration" in value:
        import capo_bedrock_agent.types.context_enrichment_configuration

        out["contextEnrichmentConfiguration"] = (
            capo_bedrock_agent.types.context_enrichment_configuration.serialize_json(
                value["context_enrichment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorIngestionConfiguration:
    out: VectorIngestionConfiguration = {}  # type: ignore[typeddict-item]
    if "chunkingConfiguration" in data:
        import capo_bedrock_agent.types.chunking_configuration

        out["chunking_configuration"] = (
            capo_bedrock_agent.types.chunking_configuration.deserialize_json(
                data["chunkingConfiguration"]
            )
        )
    if "customTransformationConfiguration" in data:
        import capo_bedrock_agent.types.custom_transformation_configuration

        out["custom_transformation_configuration"] = (
            capo_bedrock_agent.types.custom_transformation_configuration.deserialize_json(
                data["customTransformationConfiguration"]
            )
        )
    if "parsingConfiguration" in data:
        import capo_bedrock_agent.types.parsing_configuration

        out["parsing_configuration"] = (
            capo_bedrock_agent.types.parsing_configuration.deserialize_json(
                data["parsingConfiguration"]
            )
        )
    if "contextEnrichmentConfiguration" in data:
        import capo_bedrock_agent.types.context_enrichment_configuration

        out["context_enrichment_configuration"] = (
            capo_bedrock_agent.types.context_enrichment_configuration.deserialize_json(
                data["contextEnrichmentConfiguration"]
            )
        )
    return out
