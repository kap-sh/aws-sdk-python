"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EmbeddingModelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration


class EmbeddingModelConfiguration(TypedDict):
    bedrock_embedding_model_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration.BedrockEmbeddingModelConfiguration"
    ]
    """<p>The vector configuration details on the Bedrock embeddings model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddingModelConfiguration) -> dict:
    out: dict = {}
    if "bedrock_embedding_model_configuration" in value:
        import aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration

        out["bedrockEmbeddingModelConfiguration"] = (
            aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration.serialize_json(
                value["bedrock_embedding_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmbeddingModelConfiguration:
    out: EmbeddingModelConfiguration = {}  # type: ignore[typeddict-item]
    if "bedrockEmbeddingModelConfiguration" in data:
        import aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration

        out["bedrock_embedding_model_configuration"] = (
            aws_sdk_bedrock_agent.types.bedrock_embedding_model_configuration.deserialize_json(
                data["bedrockEmbeddingModelConfiguration"]
            )
        )
    return out
