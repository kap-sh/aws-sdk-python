"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.video_metadata

VideoMetadataList: TypeAlias = list[
    "aws_sdk_rekognition.types.video_metadata.VideoMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoMetadataList) -> list:
    import aws_sdk_rekognition.types.video_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.video_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VideoMetadataList:
    import aws_sdk_rekognition.types.video_metadata

    out: VideoMetadataList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.video_metadata.deserialize_aws_json_1_1(item)
        )
    return out
