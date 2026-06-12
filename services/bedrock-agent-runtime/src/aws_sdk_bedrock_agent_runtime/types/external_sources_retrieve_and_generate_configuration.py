"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExternalSourcesRetrieveAndGenerateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn
    import aws_sdk_bedrock_agent_runtime.types.external_sources
    import aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration

class ExternalSourcesRetrieveAndGenerateConfiguration(TypedDict):
    model_arn: "aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The model Amazon Resource Name (ARN) for the external source wrapper object in the <code>retrieveAndGenerate</code> function.</p>"""
    sources: "aws_sdk_bedrock_agent_runtime.types.external_sources.ExternalSources"
    """<p>The document for the external source wrapper object in the <code>retrieveAndGenerate</code> function.</p>"""
    generation_configuration: NotRequired["aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration.ExternalSourcesGenerationConfiguration"]
    """<p>The prompt used with the external source wrapper object with the <code>retrieveAndGenerate</code> function.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourcesRetrieveAndGenerateConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    import aws_sdk_bedrock_agent_runtime.types.external_sources
    out["sources"] = aws_sdk_bedrock_agent_runtime.types.external_sources.serialize_json(value["sources"])
    if "generation_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration
        out["generationConfiguration"] = aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration.serialize_json(value["generation_configuration"])
    return out


def deserialize_json(data: dict) -> ExternalSourcesRetrieveAndGenerateConfiguration:
    out: ExternalSourcesRetrieveAndGenerateConfiguration = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("ExternalSourcesRetrieveAndGenerateConfiguration.model_arn required")
    if "sources" in data:
        import aws_sdk_bedrock_agent_runtime.types.external_sources
        out["sources"] = aws_sdk_bedrock_agent_runtime.types.external_sources.deserialize_json(data["sources"])
    else:
        raise DeserializationError("ExternalSourcesRetrieveAndGenerateConfiguration.sources required")
    if "generationConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration
        out["generation_configuration"] = aws_sdk_bedrock_agent_runtime.types.external_sources_generation_configuration.deserialize_json(data["generationConfiguration"])
    return out