"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VideoConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.video_segmentation_configuration


class VideoConfiguration(TypedDict, closed=True):
    segmentation_configuration: "capo_bedrock_agent.types.video_segmentation_configuration.VideoSegmentationConfiguration"
    """<p>Configuration for segmenting video content during processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.video_segmentation_configuration

    out["segmentationConfiguration"] = (
        capo_bedrock_agent.types.video_segmentation_configuration.serialize_json(
            value["segmentation_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoConfiguration:
    out: VideoConfiguration = {}  # type: ignore[typeddict-item]
    if "segmentationConfiguration" in data:
        import capo_bedrock_agent.types.video_segmentation_configuration

        out["segmentation_configuration"] = (
            capo_bedrock_agent.types.video_segmentation_configuration.deserialize_json(
                data["segmentationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "VideoConfiguration.segmentation_configuration required"
        )
    return out
