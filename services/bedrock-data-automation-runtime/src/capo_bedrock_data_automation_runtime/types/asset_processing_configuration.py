"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AssetProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration


class AssetProcessingConfiguration(TypedDict, closed=True):
    video: NotRequired[
        "capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration.VideoAssetProcessingConfiguration"
    ]
    """Video asset processing configuration"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetProcessingConfiguration) -> dict:
    out: dict = {}
    if "video" in value:
        import capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration

        out["video"] = (
            capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration.serialize_aws_json_1_1(
                value["video"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetProcessingConfiguration:
    out: AssetProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if "video" in data:
        import capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration

        out["video"] = (
            capo_bedrock_data_automation_runtime.types.video_asset_processing_configuration.deserialize_aws_json_1_1(
                data["video"]
            )
        )
    return out
