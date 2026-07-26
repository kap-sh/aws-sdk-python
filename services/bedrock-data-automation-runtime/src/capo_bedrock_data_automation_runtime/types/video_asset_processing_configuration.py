"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#VideoAssetProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.video_segment_configuration


class VideoAssetProcessingConfiguration(TypedDict, closed=True):
    segment_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.video_segment_configuration.VideoSegmentConfiguration"
    ]
    """Delimits the segment of the input that will be processed"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoAssetProcessingConfiguration) -> dict:
    out: dict = {}
    if "segment_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.video_segment_configuration

        out["segmentConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.video_segment_configuration.serialize_aws_json_1_1(
                value["segment_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VideoAssetProcessingConfiguration:
    out: VideoAssetProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if "segmentConfiguration" in data:
        import capo_bedrock_data_automation_runtime.types.video_segment_configuration

        out["segment_configuration"] = (
            capo_bedrock_data_automation_runtime.types.video_segment_configuration.deserialize_aws_json_1_1(
                data["segmentConfiguration"]
            )
        )
    return out
