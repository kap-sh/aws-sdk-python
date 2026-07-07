"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeatureConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.customization_feature_content_moderation_config


class CustomizationFeatureConfig(TypedDict, closed=True):
    content_moderation: NotRequired[
        "aws_sdk_rekognition.types.customization_feature_content_moderation_config.CustomizationFeatureContentModerationConfig"
    ]
    """<p>Configuration options for Custom Moderation training.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationFeatureConfig) -> dict:
    out: dict = {}
    if "content_moderation" in value:
        import aws_sdk_rekognition.types.customization_feature_content_moderation_config

        out["ContentModeration"] = (
            aws_sdk_rekognition.types.customization_feature_content_moderation_config.serialize_aws_json_1_1(
                value["content_moderation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizationFeatureConfig:
    out: CustomizationFeatureConfig = {}  # type: ignore[typeddict-item]
    if "ContentModeration" in data:
        import aws_sdk_rekognition.types.customization_feature_content_moderation_config

        out["content_moderation"] = (
            aws_sdk_rekognition.types.customization_feature_content_moderation_config.deserialize_aws_json_1_1(
                data["ContentModeration"]
            )
        )
    return out
