"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_type

SegmentTypes: TypeAlias = list["aws_sdk_rekognition.types.segment_type.SegmentType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentTypes) -> list:
    import aws_sdk_rekognition.types.segment_type

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.segment_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SegmentTypes:
    import aws_sdk_rekognition.types.segment_type

    out: SegmentTypes = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.segment_type.deserialize_aws_json_1_1(item)
        )
    return out
