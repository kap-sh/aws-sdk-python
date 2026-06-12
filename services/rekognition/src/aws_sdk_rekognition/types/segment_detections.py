"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_detection

SegmentDetections: TypeAlias = list[
    "aws_sdk_rekognition.types.segment_detection.SegmentDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentDetections) -> list:
    import aws_sdk_rekognition.types.segment_detection

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.segment_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SegmentDetections:
    import aws_sdk_rekognition.types.segment_detection

    out: SegmentDetections = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.segment_detection.deserialize_aws_json_1_1(item)
        )
    return out
