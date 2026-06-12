"""Generated from Smithy shape ``com.amazonaws.rekognition#AudioMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.audio_metadata

AudioMetadataList: TypeAlias = list[
    "aws_sdk_rekognition.types.audio_metadata.AudioMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AudioMetadataList) -> list:
    import aws_sdk_rekognition.types.audio_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.audio_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AudioMetadataList:
    import aws_sdk_rekognition.types.audio_metadata

    out: AudioMetadataList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.audio_metadata.deserialize_aws_json_1_1(item)
        )
    return out
