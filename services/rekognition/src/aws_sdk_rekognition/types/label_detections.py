"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.label_detection

LabelDetections: TypeAlias = list[
    "aws_sdk_rekognition.types.label_detection.LabelDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetections) -> list:
    import aws_sdk_rekognition.types.label_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.label_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LabelDetections:
    import aws_sdk_rekognition.types.label_detection

    out: LabelDetections = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.label_detection.deserialize_aws_json_1_1(item)
        )
    return out
