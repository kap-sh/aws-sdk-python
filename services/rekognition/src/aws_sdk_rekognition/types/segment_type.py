"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentType``."""

from typing import Literal, TypeAlias, cast

SegmentType: TypeAlias = Literal[
    "TECHNICAL_CUE",
    "SHOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SegmentType:
    return cast(SegmentType, data)
