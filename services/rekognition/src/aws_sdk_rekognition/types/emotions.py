"""Generated from Smithy shape ``com.amazonaws.rekognition#Emotions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.emotion

Emotions: TypeAlias = list["aws_sdk_rekognition.types.emotion.Emotion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Emotions) -> list:
    import aws_sdk_rekognition.types.emotion

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.emotion.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Emotions:
    import aws_sdk_rekognition.types.emotion

    out: Emotions = []
    for item in data:
        out.append(aws_sdk_rekognition.types.emotion.deserialize_aws_json_1_1(item))
    return out
