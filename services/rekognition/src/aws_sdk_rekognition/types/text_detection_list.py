"""Generated from Smithy shape ``com.amazonaws.rekognition#TextDetectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.text_detection

TextDetectionList: TypeAlias = list[
    "aws_sdk_rekognition.types.text_detection.TextDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDetectionList) -> list:
    import aws_sdk_rekognition.types.text_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.text_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TextDetectionList:
    import aws_sdk_rekognition.types.text_detection

    out: TextDetectionList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.text_detection.deserialize_aws_json_1_1(item)
        )
    return out
