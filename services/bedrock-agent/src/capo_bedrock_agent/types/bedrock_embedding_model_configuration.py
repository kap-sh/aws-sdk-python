"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockEmbeddingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.audio_configurations
    import capo_bedrock_agent.types.dimensions
    import capo_bedrock_agent.types.embedding_data_type
    import capo_bedrock_agent.types.video_configurations


class BedrockEmbeddingModelConfiguration(TypedDict, closed=True):
    dimensions: NotRequired["capo_bedrock_agent.types.dimensions.Dimensions"]
    """<p>The dimensions details for the vector configuration used on the Bedrock embeddings model.</p>"""
    embedding_data_type: NotRequired[
        "capo_bedrock_agent.types.embedding_data_type.EmbeddingDataType"
    ]
    r"""<p>The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html\">Supported embeddings models</a> for information on the available models and their vector data types.</p>"""
    audio: NotRequired[
        "capo_bedrock_agent.types.audio_configurations.AudioConfigurations"
    ]
    """<p>Configuration settings for processing audio content in multimodal knowledge bases.</p>"""
    video: NotRequired[
        "capo_bedrock_agent.types.video_configurations.VideoConfigurations"
    ]
    """<p>Configuration settings for processing video content in multimodal knowledge bases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEmbeddingModelConfiguration) -> dict:
    out: dict = {}
    if "dimensions" in value:
        out["dimensions"] = value["dimensions"]
    if "embedding_data_type" in value:
        import capo_bedrock_agent.types.embedding_data_type

        out["embeddingDataType"] = (
            capo_bedrock_agent.types.embedding_data_type.serialize_json(
                value["embedding_data_type"]
            )
        )
    if "audio" in value:
        import capo_bedrock_agent.types.audio_configurations

        out["audio"] = capo_bedrock_agent.types.audio_configurations.serialize_json(
            value["audio"]
        )
    if "video" in value:
        import capo_bedrock_agent.types.video_configurations

        out["video"] = capo_bedrock_agent.types.video_configurations.serialize_json(
            value["video"]
        )
    return out


def deserialize_json(data: dict) -> BedrockEmbeddingModelConfiguration:
    out: BedrockEmbeddingModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dimensions") is not None:
        out["dimensions"] = data["dimensions"]
    if data.get("embeddingDataType") is not None:
        import capo_bedrock_agent.types.embedding_data_type

        out["embedding_data_type"] = (
            capo_bedrock_agent.types.embedding_data_type.deserialize_json(
                data["embeddingDataType"]
            )
        )
    if data.get("audio") is not None:
        import capo_bedrock_agent.types.audio_configurations

        out["audio"] = capo_bedrock_agent.types.audio_configurations.deserialize_json(
            data["audio"]
        )
    if data.get("video") is not None:
        import capo_bedrock_agent.types.video_configurations

        out["video"] = capo_bedrock_agent.types.video_configurations.deserialize_json(
            data["video"]
        )
    return out
