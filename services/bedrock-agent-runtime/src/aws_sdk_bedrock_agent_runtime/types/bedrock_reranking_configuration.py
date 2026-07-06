"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockRerankingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration


class BedrockRerankingConfiguration(TypedDict, closed=True):
    number_of_results: NotRequired["int"]
    """<p>The number of results to return after reranking.</p>"""
    model_configuration: "aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration.BedrockRerankingModelConfiguration"
    """<p>Contains configurations for a reranker model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockRerankingConfiguration) -> dict:
    out: dict = {}
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    import aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration

    out["modelConfiguration"] = (
        aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> BedrockRerankingConfiguration:
    out: BedrockRerankingConfiguration = {}  # type: ignore[typeddict-item]
    if "numberOfResults" in data:
        out["number_of_results"] = data["numberOfResults"]
    if "modelConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration

        out["model_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.bedrock_reranking_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "BedrockRerankingConfiguration.model_configuration required"
        )
    return out
