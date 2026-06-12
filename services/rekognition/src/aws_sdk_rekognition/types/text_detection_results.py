"""Generated from Smithy shape ``com.amazonaws.rekognition#TextDetectionResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.text_detection_result

TextDetectionResults: TypeAlias = list[
    "aws_sdk_rekognition.types.text_detection_result.TextDetectionResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDetectionResults) -> list:
    import aws_sdk_rekognition.types.text_detection_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.text_detection_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TextDetectionResults:
    import aws_sdk_rekognition.types.text_detection_result

    out: TextDetectionResults = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.text_detection_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
