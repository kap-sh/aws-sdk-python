"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AudioConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.audio_segmentation_configuration


class AudioConfiguration(TypedDict):
    segmentation_configuration: "aws_sdk_bedrock_agent.types.audio_segmentation_configuration.AudioSegmentationConfiguration"
    """<p>Configuration for segmenting audio content during processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.audio_segmentation_configuration

    out["segmentationConfiguration"] = (
        aws_sdk_bedrock_agent.types.audio_segmentation_configuration.serialize_json(
            value["segmentation_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioConfiguration:
    out: AudioConfiguration = {}  # type: ignore[typeddict-item]
    if "segmentationConfiguration" in data:
        import aws_sdk_bedrock_agent.types.audio_segmentation_configuration

        out["segmentation_configuration"] = (
            aws_sdk_bedrock_agent.types.audio_segmentation_configuration.deserialize_json(
                data["segmentationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AudioConfiguration.segmentation_configuration required"
        )
    return out
