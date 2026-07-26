"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentTypesInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.segment_type_info

SegmentTypesInfo: TypeAlias = list[
    "capo_rekognition.types.segment_type_info.SegmentTypeInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentTypesInfo) -> list:
    import capo_rekognition.types.segment_type_info

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.segment_type_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SegmentTypesInfo:
    import capo_rekognition.types.segment_type_info

    out: SegmentTypesInfo = []
    for item in data:
        out.append(
            capo_rekognition.types.segment_type_info.deserialize_aws_json_1_1(item)
        )
    return out
