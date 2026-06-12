"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisOperationsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config


class MediaAnalysisOperationsConfig(TypedDict):
    detect_moderation_labels: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config.MediaAnalysisDetectModerationLabelsConfig"
    ]
    """<p>Contains configuration options for a DetectModerationLabels job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisOperationsConfig) -> dict:
    out: dict = {}
    if "detect_moderation_labels" in value:
        import aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config

        out["DetectModerationLabels"] = (
            aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config.serialize_aws_json_1_1(
                value["detect_moderation_labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisOperationsConfig:
    out: MediaAnalysisOperationsConfig = {}  # type: ignore[typeddict-item]
    if "DetectModerationLabels" in data:
        import aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config

        out["detect_moderation_labels"] = (
            aws_sdk_rekognition.types.media_analysis_detect_moderation_labels_config.deserialize_aws_json_1_1(
                data["DetectModerationLabels"]
            )
        )
    return out
