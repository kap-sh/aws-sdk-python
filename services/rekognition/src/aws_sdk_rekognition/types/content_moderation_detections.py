"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.content_moderation_detection

ContentModerationDetections: TypeAlias = list[
    "aws_sdk_rekognition.types.content_moderation_detection.ContentModerationDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentModerationDetections) -> list:
    import aws_sdk_rekognition.types.content_moderation_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.content_moderation_detection.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContentModerationDetections:
    import aws_sdk_rekognition.types.content_moderation_detection

    out: ContentModerationDetections = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.content_moderation_detection.deserialize_aws_json_1_1(
                item
            )
        )
    return out
